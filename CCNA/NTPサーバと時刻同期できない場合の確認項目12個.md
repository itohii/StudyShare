# NTPサーバと時刻同期できない場合の確認項目12個
　指定したNTPサーバの[IPアドレス]は正しいか
　ネットワーク機器（NTP Client）で設定したタイムゾーンの設定は正しいか
　ネットワーク機器（NTP Client）から、NTPサーバにIP到達性があるか
　ネットワーク機器（NTP Client）に複数のI/Fがある場合、送信元I/Fを指定しているか
　NTP Client ⇔ NTP Server間にFirewallがある場合、NTPパケットは許可されているか
　ネットワーク機器（NTP Client）で、NTP Clientの設定を削除して再度設定する
　ネットワーク機器（NTP Client）側で、時刻設定を手動で設定する
　指定しているNTPサーバが、Windows Serverではないことを確認
　指定しているNTPサーバが、SNTP Serverではないことを確認
　指定しているNTPサーバが、上位NTPサーバと正常に同期できていることを確認
　指定しているNTPサーバ側で、認証設定がされていないか
　構築環境で可能であるなら、ネットワーク機器（NTP Client）を再起動
