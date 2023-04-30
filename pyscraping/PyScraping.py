import requests
from bs4 import BeautifulSoup
from sys import exit as logout

class PyScraping:
  def __init__(self, url):
    self.url = url
    self.WHITE = '\x1b[1;97m'
    self.RED = '\x1b[1;91m'
    self.GREEN = '\x1b[1;92m'
    self.YELLOW = '\x1b[1;93m'
    self.PURPLE = '\x1b[1;94m'
    self.BLUE = '\x1b[1;96m'
    self.DEFAULT = '\x1b[0m'
    self.success = f"{self.WHITE}[{self.GREEN}!{self.WHITE}]"
    self.failed = f"{self.WHITE}[{self.RED}!{self.WHITE}]"
    try:
      response = requests.get(url)
      self.soup = BeautifulSoup(response.content, 'html.parser')
    except Exception:
        logout(print(f"""\n{self.failed} Invalid URL or Domain.{self.DEFAULT}"""))
  
  def title(self):
    if self.url:
        return self.soup.title.string
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def charset(self):
    if self.url:
      self.response.encoding = 'UTF-8'
      meta_charset = self.soup.find('meta', charset=True)
      if meta_charset:
        return meta_charset['charset']
      else:
        logout(print(f"\n{self.failed} No charset found in meta tags.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def viewport(self):
    if self.url:
      viewport_tag = self.soup.find('meta', attrs={'name': 'viewport'})
      if viewport_tag:
        viewport = viewport_tag['content']
        return viewport.split(",")
      else:
        logout(print(f"\n{self.failed} No viewport meta tag found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def viewportString(self):
    if self.url:
      viewport_tag = self.soup.find('meta', attrs={'name': 'viewport'})
      if viewport_tag:
        return viewport_tag['content']
      else:
        logout(print(f"\n{self.failed} No viewport meta tag found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def canonical(self):
    if self.url:
      canonical_tag = self.soup.find('link', attrs={'rel': 'canonical'})
      if canonical_tag:
        return canonical_tag['href']
      else:
        logout(print(f"\n{self.failed} No canonical link found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def contentType(self):
    if self.url:
      content_type_tag = self.soup.find('meta', attrs={'http-equiv': 'Content-Type'})
      if content_type_tag:
        return content_type_tag['content']
      else:
        logout(print(f"\n{self.failed} No Content-Type meta tag found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def csrfToken(self):
    if self.url:
      csrf_token_tag = self.soup.find('meta', attrs={'name': 'csrf-token'})
      if csrf_token_tag:
        return csrf_token_tag['content']
      else:
        logout(print(f"\n{self.failed} No CSRF Token meta tag found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
  
  def author(self):
    if self.url:
      author_tag = self.soup.find('meta', attrs={'name': 'author'})
      if author_tag:
        return author_tag['content']
      else:
        logout(print(f"\n{self.failed} No Author meta tag found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
  
  def description(self):
    if self.url:
      description_tag = self.soup.find('meta', attrs={'name': 'description'})
      if description_tag:
        return description_tag['content']
      else:
        logout(print(f"\n{self.failed} No Description meta tag found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
  
  def image(self):
    if self.url:
      image_tag = self.soup.find('meta', attrs={'property': 'og:image'})
      if image_tag:
        return image_tag['content']
      else:
        logout(print(f"\n{self.failed} No Image meta tag found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
  
  def keywords(self):
    if self.url:
      keywords_tag = self.soup.find('meta', attrs={'name': 'keywords'})
      if keywords_tag:
        keywords = keywords_tag['content']
        return keywords.split(",")
      else:
        logout(print(f"\n{self.failed} No Keywords meta tag found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def keywordString(self):
    if self.url:
      keywords_tag = self.soup.find('meta', attrs={'name': 'keywords'})
      if keywords_tag:
        return keywords_tag['content']
      else:
        logout(print(f"\n{self.failed} No Keywords meta tag found.{self.DEFAULT}"))
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def openGraph(self, openGraph = False):
    if self.url:
      if openGraph:
        og = self.soup.find('meta', attrs={'property': openGraph})
        if og:
          return og['content']
        else:
          logout(print(f"\n{self.failed} No {openGraph} meta tag found.{self.DEFAULT}"))
      else:
        og_site_name = self.soup.find('meta', attrs={'property': 'og:site_name'})
        og_type = self.soup.find('meta', attrs={'property': 'og:type'})
        og_title = self.soup.find('meta', attrs={'property': 'og:title'})
        og_description = self.soup.find('meta', attrs={'property': 'og:description'})
        og_url = self.soup.find('meta', attrs={'property': 'og:url'})
        og_image = self.soup.find('meta', attrs={'property': 'og:image'})
      
      if og_site_name:
        site_name = og_site_name['content']
      else:
        site_name = False
      if og_type:
        type = og_type['content']
      else:
        type = False
      if og_title:
        title = og_title['content']
      else:
        title = False
      if og_description:
        description = og_description['content']
      else:
        description = False
      if og_url:
        url = og_url['content']
      else:
        url = False
      if og_image:
        image = og_image['content']
      else:
        image = False
        
      array = {}
      array["og:site_name"] = site_name
      array["og:type"] = type
      array["og:title"] = title
      array["og:description"] = description
      array["og:url"] = url
      array["og:image"] = image
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def twitterCard(self, twitterCard = False):
    if self.url:
      if twitterCard:
        tc = twitterCard
        twitter = self.soup.find('meta', attrs={'name': twitterCard})
        if twitter:
          return twitter['content']
        else:
          logout(print(f"\n{self.failed} No {tc} meta tag found.{self.DEFAULT}"))
      else:
        td = "twitter:description"
        twitter_card = self.soup.find('meta', attrs={'name': 'twitter:card'})
        twitter_title = self.soup.find('meta', attrs={'name': 'twitter:title'})
        twitter_description = self.soup.find('meta', attrs={'name': td})
        twitter_url = self.soup.find('meta', attrs={'name': 'twitter:url'})
        twitter_image = self.soup.find('meta', attrs={'name': 'twitter:image'})
      
      if twitter_card:
        card = twitter_card['content']
      else:
        card = False
      if twitter_title:
        title = twitter_title['content']
      else:
        title = False
      if twitter_description:
        description = twitter_description['content']
      else:
        description = False
      if twitter_url:
        url = twitter_url['content']
      else:
        url = False
      if twitter_image:
        image = twitter_image['content']
      else:
        image = False
        
      array = {}
      array["twitter:card"] = card
      array["twitter:title"] = title
      array["twitter:description"] = description
      array["twitter:url"] = url
      array["twitter:image"] = image
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def h1(self):
    if self.url:
      h1_tags = self.soup.find_all('h1')
      array = []
      for h1 in h1_tags:
        array.append(h1.text)
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def h2(self):
    if self.url:
      h2_tags = self.soup.find_all('h2')
      array = []
      for h2 in h2_tags:
        array.append(h2.text)
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def h3(self):
    if self.url:
      h3_tags = self.soup.find_all('h3')
      array = []
      for h3 in h3_tags:
        array.append(h3.text)
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
      
  def h4(self):
    if self.url:
      h4_tags = self.soup.find_all('h4')
      array = []
      for h4 in h4_tags:
        array.append(h4.text)
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
 
  def h5(self):
    if self.url:
      h5_tags = self.soup.find_all('h5')
      array = []
      for h5 in h5_tags:
        array.append(h5.text)
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
  
  def h6(self):
    if self.url:
      h6_tags = self.soup.find_all('h6')
      array = []
      for h6 in h6_tags:
        array.append(h6.text)
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))

  def p(self):
    if self.url:
      p_tags = self.soup.find_all('p')
      array = []
      for p in p_tags:
        array.append(p.text)
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
 
  def ul(self):
    if self.url:
      array = []
      lists = self.soup.find_all("ul")
      for lst in lists:
        items = lst.find_all("li")
        for item in items:
          array.append(item.text.strip())
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
  
  def ol(self):
    if self.url:
      array = []
      lists = self.soup.find_all("ul")
      for lst in lists:
        items = lst.find_all("li")
        for item in items:
          array.append(item.text.strip())
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
 
  def images(self):
    if self.url:
      array = []
      images = self.soup.find_all("img")
      for img in images:
        array.append(img.get("src"))
      return array
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
 
  def imagesDetails(self):
    if self.url:
      images = self.soup.find_all("img")
      image_details = []
      for img in images:
        img_url = img.get("src")
        alt_text = img.get("alt")
        title = img.get("title")
        img_dict = {
          "url": img_url,
          "alt_text": alt_text,
          "title": title
        }
      image_details.append(img_dict)
      return image_details
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
 
  def links(self):
    if self.url:
      links = []
      for link in self.soup.find_all("a"):
        href = link.get("href")
        if href is not None:
          links.append(href)
      return links
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
 
  def linksDetails(self):
    if self.url:
      links = self.soup.find_all('a')
      result = []
      for link in links:
        url = link.get('href')
        protocol = url.split(':')[0] if url and ':' in url else ''
        text = link.text.strip()
        title = link.get('title', '')
        target = link.get('target', '')
        rel = link.get('rel')
        isNowFollow = 'nofollow' in rel if rel is not None else False
        isUGC = 'ugc' in rel if rel is not None else False
        isNoopener = 'noopener' in rel if rel is not None else False
        isNoreferrer = 'noreferrer' in rel if rel is not None else False
        result.append({
          'url': url,
          'protocol': protocol,
          'text': text,
          'title': title,
          'target': target,
          'rel': rel,
          'isNowFollow': isNowFollow,
          'isUGC': isUGC,
          'isNoopener': isNoopener,
          'isNoreferrer': isNoreferrer
        })
      return result
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))
 
  def filter(self, element, attribute):
    if self.url:
      return self.soup.find(element, attribute)
    else:
      logout(print(f"\n{self.failed} URL cannot be empty.{self.DEFAULT}"))