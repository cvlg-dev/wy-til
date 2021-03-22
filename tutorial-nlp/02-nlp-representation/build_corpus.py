import numpy as np
import argparse
import re


class TokenBuilder:

    def __init__(self, text):
        self.original_text = text

    def clean_text(self):
        target_text = self.original_text

        ## remove line breaks
        target_text = target_text.lower()
        target_text = target_text.replace(" \n\n", " ")
        target_text = target_text.replace(" \\n", " ")
        target_text = target_text.replace("\\n", " ")
        target_text = target_text.replace(" \\u", " ")
        target_text = target_text.replace("\\u", " ")
        target_text = target_text.replace(r" \u", " ")
        target_text = target_text.replace(r"\u", " ")
        target_text = target_text.replace("\n\n", " ")
        target_text = target_text.replace(" \n", " ")
        target_text = target_text.replace("\n", " ")
        target_text = target_text.replace("\xa0", " ")
        target_text = target_text.replace("\\xa0", " ")
        target_text = target_text.replace("\\ ", "")
        target_text = target_text.replace(" \\", "")
        target_text = target_text.replace("\\\\\3000", "")
        target_text = target_text.replace("(주)", "")
        target_text = target_text.replace("㈜", "")
        target_text = target_text.replace("ⓒ", "")

        ## remove URL
        target_text = re.sub("\(?(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?\)?", "",
                           target_text)
        ## remove writer
        target_text = re.sub("[가-힣a-zA-Z]{3} [가-힣a-zA-Z]{4} 기자", "", target_text)
        target_text = re.sub("[가-힣a-zA-Z]{3} ?기자", "", target_text)
        target_text = re.sub("[가-힣a-zA-Z]{2} ?기자", "", target_text)

        ## remove square brackets and content
        target_text = re.sub(r'\[.*?\]', '', target_text)
        target_text = re.sub(r'\<.*?\>', '', target_text)
        target_text = re.sub(r'\＜.*?\＞', '', target_text)
        target_text = re.sub(r'\(.*?\)', '', target_text)

        ## remove copyright text
        target_text = re.sub(r"무단 ?전재.+?재배포 ?금지", '', target_text)

        ## remove email address
        target_text = re.sub(pattern="(\([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)\)", repl='', string=target_text)
        target_text = re.sub(pattern="([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", repl='', string=target_text)
        target_text = re.sub(pattern="(\([a-zA-Z0-9_.+-]+@)\)", repl='', string=target_text)
        target_text = re.sub(pattern="([a-zA-Z0-9_.+-]+@)", repl='', string=target_text)

        ## remove provider specific text
        target_text = target_text.replace("성공을 부르는 습관 한경닷컴", "")
        target_text = target_text.replace("증시분석 전문기자 로봇 ET", "")
        target_text = re.sub("현대증권 [가-힣]+ 금융상품팀장", "", target_text)
        target_text = target_text.replace(r"경북일보 - 굿데이 굿뉴스 & kyongbuk.co.kr", "")
        target_text = target_text.replace("기자와 카톡으로 채팅하기", "")
        target_text = target_text.replace("노컷뉴스 영상 구독하기", "")
        target_text = target_text.replace("공시 전문으로 이동", "")
        target_text = target_text.replace("스톡봇", "")
        target_text = re.sub("이 기사는 국민일보와 엠로보가 개발한 증권뉴스 전용 인공지능 로봇+", "", target_text)
        target_text = target_text.replace("동아닷컴 it전문", "")
        target_text = re.sub("리뷰 의뢰는 .* ?으로 연락하시기 바랍니다", "", target_text)
        target_text = target_text.replace("이슈투데이였습니다.", "")
        target_text = re.sub("[가-힣]{3} jb금융지주 상무", "", target_text)
        target_text = target_text.replace("새전북신문(www.sjbnews.com)", "")

        ## replace redundant spaces
        target_text = re.sub(pattern='\.\s+', repl='. ', string=target_text)
        
        self.cleaned_text = target_text

    def build_idx(self):
        text = self.cleaned_text
        tokens = text.split(' ')

        self.word2id = {}
        self.id2word = {}

        for word in tokens:
            if word not in self.word2id:
                new_id = len(self.word2id)
                self.word2id[word] = new_id
                self.id2word[new_id] = word

        self.corpus = np.array([self.word2id[w] for w in tokens])

