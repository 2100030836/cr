import requests
from bs4 import BeautifulSoup

def fetch_live_score():
    url = 'https://www.cricbuzz.com/cricket-match/live-scores'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {'error': 'Failed to fetch data from Cricbuzz'}

    soup = BeautifulSoup(response.text, 'html.parser')
    matches = []
    for match in soup.select('.cb-mtch-lst .cb-lv-scrs-col'):
        title_elem = match.select_one('.cb-ovr-flo.cb-lv-scr-mtch-hdr')
        status_elem = match.select_one('.cb-ovr-flo.cb-text-live, .cb-ovr-flo.cb-text-complete, .cb-ovr-flo.cb-text-preview')
        score_elem = match.select_one('.cb-ovr-flo.cb-text-live')
        title = title_elem.get_text(strip=True) if title_elem else ''
        status = status_elem.get_text(strip=True) if status_elem else ''
        score = score_elem.get_text(strip=True) if score_elem else ''
        teams = [t.get_text(strip=True) for t in match.select('.cb-ovr-flo span')]
        matches.append({
            'title': title,
            'status': status,
            'score': score,
            'teams': teams
        })
    return {'matches': matches}
