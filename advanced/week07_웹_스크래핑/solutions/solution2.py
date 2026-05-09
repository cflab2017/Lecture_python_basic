import requests

USER = "python"
r = requests.get(f"https://api.github.com/users/{USER}/repos",
    params={"per_page": 100},
    headers={"User-Agent": "study"},
    timeout=10)
r.raise_for_status()
repos = r.json()

print(f"사용자: {USER}")
print(f"저장소 개수: {len(repos)}")
ranked = sorted(repos, key=lambda x: -x["stargazers_count"])
for i, repo in enumerate(ranked[:10], 1):
    print(f"{i}. {repo['name']} - {repo['stargazers_count']} stars")
