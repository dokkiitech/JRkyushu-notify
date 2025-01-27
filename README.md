# 🌆 JR九州 遅延情報 Discord Bot

![JR九州遅延情報 Bot](https://img.shields.io/badge/Discord-Bot-blue?style=for-the-badge&logo=discord)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)

**JR九州の運行遅延情報をリアルタイムで取得し、Discordに通知するBotです。**

---

## 🔧 機能一覧

- JR九州の運行情報を取得
- エリアごとの詳細な遅延状況を表示
- 運行情報の最終更新時間を通知
- メンションするだけで簡単に使用可能

---

## 🚀 デモ

以下のように、Botをメンションすると最新の運行情報が表示されます：

```
🚆 JR九州運行情報（最終更新: 2025年01月27日 19時25分）
取得時刻: 2025年01月28日 01時07分

福岡・北九州エリア: 遅れの情報はありません。
大分エリア: 遅れの情報はありません。
佐賀・長崎エリア: 遅れの情報はありません。
熊本エリア: 長期の運転見合せ区間があります。
宮崎エリア: 遅れの情報はありません。
鷺崎島エリア: 長期の運転見合せ区間があります。
九州新幹線: 遅れ等が発生しています。
西九州新幹線: 遅れの情報はありません。
```

---

## 📦 必要なライブラリ

このプロジェクトを動かすためには以下のPythonライブラリが必要です：

- [requests](https://pypi.org/project/requests/)：データ取得
- [discord.py](https://pypi.org/project/discord.py/)：Discord Bot操作
- [python-dotenv](https://pypi.org/project/python-dotenv/)：環境変数管理

---

## 💻 インストール方法

1. **リポジトリをクローン**
   ```bash
   git clone https://github.com/dokkiitech/JRkyushu-notify.git
   cd jrkyushu-discord-bot
   ```

2. **必要なライブラリをインストール**
   ```bash
   pip install requests discord.py python-dotenv
   ```

3. **`.env`ファイルを作成**
   プロジェクトフォルダ内に`.env`ファイルを作成し、以下のように記述してください：

   ```env
   DISCORD_TOKEN=あなたのDiscordBotトークン
   ```

4. **Botを起動**
   ```bash
   python bot.py
   ```

---

## 🔧 使用方法

1. BotをDiscordサーバーに招待します（Bot招待リンクを生成）。
2. サーバー内の任意のチャンネルでBotをメンション（`@BotName`）すると、最新の運行情報が取得できます。

---

## 📜 ライセンス

[MIT License](LICENSE)

このプロジェクトはMITライセンスの下で公開されています。

---

## 🤝 コントリビュート

1. リポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/新機能`)
3. 変更をコミット (`git commit -m 'Add 新機能'`)
4. ブランチをプッシュ (`git push origin feature/新機能`)
5. プルリクエストを作成

---

## 📨 お問い合わせ

ご質問や提案がある場合は、以下でお気軽にご連絡ください：

- **Email**: info@dokkiitech.com
- **Discord**: dokkiitech
