# Argus
[https://lh3.googleusercontent.com/a/AEdFTp5rHJmEwgQA-GHjw1w3CT6-hc_9h5ix0Rm5Z1mh=s96-c#.png]
code:script.js
 let line = scrapbox.Page.lines[1]
　scrapbox.PageMenu.addItem({
     title: 'Tweet',
     image: 'https://twitter.com/favicon.ico',
     onClick: () => window.open(`https://twitter.com/intent/tweet?url=${""}&text=${encodeURIComponent(scrapbox.Page.title) + " " + encodeURIComponent(location.href) + encodeURIComponent(" #Argus #学習 ") + encodeURIComponent(scrapbox.Page.lines[scrapbox.Page.lines.length - 2].text) + " " + encodeURIComponent(scrapbox.Page.lines[1].text)}`)
   })

