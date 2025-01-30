import requests

def check_url(url):
  """Checks if a URL is blocked by a firewall.

  Args:
    url: The URL to check.

  Returns:
    True if the URL is blocked, False otherwise.
  """
  try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raise an exception for bad status codes
    #print(f"Error accessing {url}")
    return False  # URL is accessible
  except requests.exceptions.RequestException as e:
    print(f"Error accessing {url}: {e}")
    return True  # Assume blocked due to an error

# Define the URLs to scan
urls = [
  "https://wftest83.fortiguard.fortinet.com/wftest/1.html",
  "https://www.bovada.lv/",
  "https://wftest83.fortiguard.fortinet.com/wftest/2.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/3.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/4.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/5.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/6.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/7.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/8.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/9.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/10.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/11.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/12.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/13.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/14.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/15.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/16.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/17.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/18.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/19.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/20.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/21.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/22.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/23.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/24.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/25.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/26.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/27.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/28.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/29.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/30.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/31.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/32.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/33.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/34.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/35.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/36.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/37.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/38.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/39.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/40.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/41.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/42.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/43.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/44.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/45.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/46.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/47.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/48.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/49.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/50.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/51.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/52.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/53.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/54.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/55.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/56.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/57.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/58.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/59.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/60.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/61.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/62.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/63.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/64.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/65.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/66.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/67.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/68.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/69.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/70.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/71.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/72.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/73.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/74.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/75.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/76.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/77.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/78.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/79.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/80.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/81.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/82.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/83.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/84.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/85.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/86.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/87.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/88.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/89.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/90.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/91.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/92.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/93.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/94.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/95.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/96.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/97.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/98.html",
  "https://wftest83.fortiguard.fortinet.com/wftest/99.html",
]

# Scan the URLs and print the blocked ones
for url in urls:
  if check_url(url):
    print(f"URL blocked: {url}")
