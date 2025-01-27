import os
import requests
import xml.etree.ElementTree as ET
import discord
from dotenv import load_dotenv
from datetime import datetime
import random

# .envファイルの読み込み
load_dotenv()

# Discordのトークンを環境変数から取得
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# JR九州の運行情報XML URL
JR_KYUSHU_XML_URL = "https://www.jrkyushu.co.jp/trains/info/data/IDS2Web.xml"

# 英語エリア名を日本語に翻訳するマッピング
AREA_NAME_MAPPING = {
    "Fukuoka-Kitakyushu": "福岡・北九州エリア",
    "Oita": "大分エリア",
    "Saga-Nagasaki": "佐賀・長崎エリア",
    "Kumamoto": "熊本エリア",
    "Miyazaki": "宮崎エリア",
    "Kagoshima": "鹿児島エリア",
    "Kyushu-Shinkansen": "九州新幹線",
    "Nishi-Kyushu-Shinkansen": "西九州新幹線",
}

# 遅延情報を取得して解析する関数
def fetch_delay_info():
    try:
        # XMLデータを取得（キャッシュ回避のためのランダムクエリ追加）
        params = {"_": random.randint(1, 1000000)}  # キャッシュ回避用パラメータ
        headers = {"Cache-Control": "no-cache", "Pragma": "no-cache"}
        response = requests.get(JR_KYUSHU_XML_URL, headers=headers, params=params)
        response.raise_for_status()

        # レスポンスからサーバーの取得時刻を記録
        fetched_time = datetime.now().strftime("%Y年%m月%d日 %H時%M分")

        # XMLデータを解析
        xml_content = response.text
        root = ET.fromstring(xml_content)

        # 最終更新時間を取得
        update_time_raw = root.find("time").text
        update_time = (
            f"{update_time_raw[:4]}年{update_time_raw[4:6]}月{update_time_raw[6:8]}日 "
            f"{update_time_raw[8:10]}時{update_time_raw[10:12]}分"
        )

        # エリアごとの運行情報を取得
        area_info = []
        for aif in root.findall(".//aif"):
            # エリア名を翻訳
            raw_area_name = aif.find("nm").text if aif.find("nm") is not None else "エリア名不明"
            area_name = AREA_NAME_MAPPING.get(raw_area_name, raw_area_name)  # 翻訳またはそのまま使用

            # 運行状況
            status = aif.find("sts").text if aif.find("sts") is not None else "ステータス不明"
            # ステータスを解釈
            if status == "0":
                delay_info = "遅れの情報はありません。"
            elif status == "1":
                delay_info = "遅れ等が発生しています。"
            elif status == "2":
                delay_info = "長期の運転見合わせ区間があります。"
            else:
                delay_info = "運行状況に問題があります。"
            area_info.append(f"{area_name}: {delay_info}")

        # 結果を整形
        area_details = "\n".join(area_info)
        result = (
            f"🚆 JR九州運行情報（最終更新: {update_time}）\n"
            f"取得時刻: {fetched_time}\n\n"
            f"{area_details}"
        )
        return result
    except Exception as e:
        return f"遅延情報の取得中にエラーが発生しました: {e}"

# Discordクライアント設定
intents = discord.Intents.default()
intents.message_content = True  # メッセージ内容取得のために有効化
client = discord.Client(intents=intents)

# Botが起動したときのイベント
@client.event
async def on_ready():
    print(f"Botが起動しました: {client.user}")

# メッセージを受信したときのイベント
@client.event
async def on_message(message):
    # Bot自身のメッセージは無視
    if message.author.bot:
        return

    # Botがメンションされた場合
    if client.user.mentioned_in(message):
        # 遅延情報を取得
        delay_info = fetch_delay_info()
        # メンションされたチャンネルに遅延情報を送信
        await message.channel.send(delay_info)

# Botを実行
client.run(DISCORD_TOKEN)