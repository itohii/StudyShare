# Tumblrのテンプレートの構造
 <html>～</html> … すべてのHTMLの要素がこのタグの内側に記述される
 <head>～</head> … META、Titleなどの要素、Faviconの指定、RSS、スタイルシートの記述などを行う
 <body>～</body> … この中にホームページのコンテンツを記述していく
 {Title} … Tumblrで指定したブログのタイトルが挿入される
 {block:SearchPage}{/block:SearchPage} … 検索の結果を表示するためのブロック要素
 {block:Posts}{/block:Posts} … 投稿された記事を表示するためのブロック要素
 {block:Pagination}{/block:Pagination} …Tumblr標準のページ送り機能を表示する
