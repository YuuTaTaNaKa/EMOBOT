from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

# 事前学習済みの日本語感情分析モデルとそのトークナイザをロード
model_name  = 'lxyuan/distilbert-base-multilingual-cased-sentiments-student'  # 一番使い勝手の良かった軽量モデルに置き換え済。より軽いモデルがあれば、それに置き換え
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name,torch_dtype=torch.float16)  # 低精度(float16)でモデルを動作させて計算量を削減

# 感情分析パイプラインの設定
nlp = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer, truncation=True, max_length=128)  # 最大文字数を128文字に設定する

# 分析対象のテキストリスト



texts = ['給料が高くて満足しています。', '給料低すぎるだろ！', '可もなく不可もなく']

# 一度にすべてのテキストを処理して結果を取得
results = nlp(texts)

# 結果を表示
for text, result in zip(texts, results):
    print('*' * 50)
    print(f'テキスト：{text}')
    print(f'感情：{result["label"]}')  # positive,negative,neutralの3種類
    print(f'感情スコア：{result["score"]:.4f}')

# """pip install Cython"""
# """pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/armv7l transformers"""
# """pip install fugashi unidic_lite"""
