# Big Brother is watching

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Web Warning
- **Points:** 1

## Provided Materials

- Text `Even Google cannot find this one`

## Solution

We need to figure out, what google can't find... [robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) file tells search engine crawlers which URLs the crawler can access on your site, so let's check it *([https://ringzer0ctf.com/robots.txt](https://ringzer0ctf.com/robots.txt))*:

```
User-agent: *
Disallow: /16bfff59f7e8343a2643bdc2ee76b2dc/
```

We see one disallowed path, so when we open it *([https://ringzer0ctf.com//16bfff59f7e8343a2643bdc2ee76b2dc/](https://ringzer0ctf.com//16bfff59f7e8343a2643bdc2ee76b2dc/)*), we get our flag.

## Final Flag

`FLAG-G5swO95w0c7R5fq0sa85nVs5dK49O04i`

*Created by [bu19akov](https://github.com/bu19akov)*