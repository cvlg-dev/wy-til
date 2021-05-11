
```bash
python saveToBento.py
```


```bash
bentoml serve KobertSentiClassifier:latest
```

```bash
curl -X POST "http://127.0.0.1:52621/predict" -H "accept: */*" -H "Content-Type: application/json" -d "{\"text\":\"이 영화는 진짜 개쓰레기여\"}"
```



- Todo
    - 모델마다 라벨 붙이기 또는 이름 붙이기