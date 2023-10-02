# Pythonチュートリアル 第3版 115ページ
 「from os import * 」ではなく、必ず「import os」を使うこと。これは os.open() がビルトインの open() 関数を隠さないようにするためだ。動作がぜんぜん違う
