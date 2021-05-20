
# KoBert Sentiment Classifier

Korean sentiment classifier trained on KoBert & NSMC dataset.

### Save model

```bash
python saveToBento.py
```

### Serve model

```bash
bentoml serve KobertSentiClassifier:latest
```

### Request model inference

```bash
curl -X POST "http://127.0.0.1:52621/predict" -H "accept: */*" -H "Content-Type: application/json" -d "{\"text\":\"이 영화는 진짜 엉망이네\"}"
```

## Deploy to GCP

1. Build bentoml latest server image

	```
	saved_path=$(bentoml get KobertSentiClassifier:latest --print-location --quiet)
	cd $saved_path
	```
	
	```
	gcloud builds submit --tag gcr.io/kobert-bentoml/kobert-senti-bentoml
	```

2. Deploy latest image in GCP run

## Todo
    - 모델마다 라벨 붙이기 또는 이름 붙이기