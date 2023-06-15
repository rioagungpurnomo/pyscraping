# PyScraping
PyScraping is a universal web-scraping util for Python, built with simplicity in mind.

## Installation
Start to do the installation.
```bash
pip install pyscraping
```

## Example
All scraping functionality can be accessed either as a function call or a property call. For example, the title can be accessed in two ways:

```python
from pyscraping.PyScraping import PyScraping

pyscraping = PyScraping("https://google.com")

print(pyscraping.title())
```

## Documentation
### `<head>` tags
#### Get Website Title
Scraping the title from a website is simple.
```python
pyscraping.title()
```
#### Get Meta Charset
To access the defined charset, you can use the following method:
```python
pyscraping.charset()
```
#### Get Meta Viewport
In some cases, such as the viewport and the meta keywords, the string is representing an array and will be provided as such:
```python
pyscraping.viewport()
```
If you need to access the original "viewport"-string, you can use `viewportString`:
```python
pyscraping.viewportString()
```
#### Get Canonical URL
The canonical URL, if given, can be accessed as shown in the example below:
```python
pyscraping.canonical()
```
#### Get Meta Content-Type
To access the content type you can use the following functionality:
```python
pyscraping.contentType()
```
#### Get Meta CSFR Token
The CSFR token method assumes that the token is stored in a meta tag with the name "csrf-token". This is the default for Laravel. You can access it using the following code:
```python
pyscraping.csrfToken()
```
#### Get Meta Author, Description and Image
The following example shows the extraction of three attributes:
- the Meta Author,
- the Meta Description and
- the Meta Image URL
```python
pyscraping.author()
pyscraping.description()
pyscraping.image()
```
#### Get Meta Keywords
The keywords meta-tag is naturally an array and will be split for your convenience:
```python
pyscraping.keywords()
```
Alternatively, you can access the original keyword string:
```python
pyscraping.keywordString()
```
#### Get Meta Open-Graph (OG) Data
Fetching open-graph data can be done:
- og:site_name
- og:type
- og:title
- og:description
- og:url
- og:image
```python
# Example
pyscraping.openGraph("og:title")

# All
pyscraping.openGraph()
```
#### Get Meta Twitter Card
Parsing the Twitter Card works similarly:
- twitter:card
- twitter:title
- twitter:description
- twitter:url
- twitter:image
```python
# Example
pyscraping.twitterCard("twitter:title")

# All
pyscraping.twitterCard()
```
### `<body>` tags
#### Get Headings by Level
There might be cases, in which all headings of a particular level should be retrieved. The example below shows how to do so:
```python
pyscraping.h1()
pyscraping.h2()
pyscraping.h3()
pyscraping.h4()
pyscraping.h5()
pyscraping.h6()
```
#### Get all Paragraphs
The following example will return a list of all paragraphs (`<p>`-tags) on the website:
```python
pyscraping.p()
```
#### Get Unordered Lists
The following example will return a list of all list (`<ul>`-tags) on the website:
```python
pyscraping.ul()
```
#### Get Ordered Lists
The following example will return a list of all list (`<ol>`-tags) on the website:
```python
pyscraping.ol()
```
#### Get all Image URLs
The following example parses a web-page for images and returns absolute image URLs as an array.
```python
pyscraping.images()
```
#### Get all Images with Details
If you are in need of more details the following requests allows you to access attributes of the image tag:
```python
pyscraping.imagesDetails()
```
#### Get all Link List
The following example parses a web-page for any links and returns an array of absolute URLs:
```python
pyscraping.links()
```
#### Get all Links with Details
If you are in need of more details you can access these in a similar way as on the images. Below is an example to access the detailed data of the first link on the page:
```python
pyscraping.linksDetails()
```
#### Custom xPath Selectors
The following examples of custom selectors should be seen as a starting point for any custom information you need to scrape.
```python
pyscraping.filter(element, attribute)
```
Example
```python
pyscraping.filter('div', 'class="container"')
```

## Donate
- [Saweria](https://saweria.co/rioagungpurnomo)
- [Trakteer](https://trakteer.id/rioagungpurnomo)
- [PayPal](https://www.paypal.me/rioagungpurnomoo)

## Contact me
Contact me via email: rioagungpurnomo@programmer.net, I'm waiting for your input or suggestions.
