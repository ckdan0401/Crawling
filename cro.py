from matplotlib.pyplot import text
import requests

res = requests.get("http://naver.com")
res.raise_for_status() #문제가 없으면 출력 있으면 에러 

# print ("응답코드 : ", res.status_code)

# if res.status_code == requests.codes.ok : # res.status_code == 200 랑 같음
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다[에러코드 : ",res.status_code,"]")
print(len(res.text))#해당 페이지에 글자수 출력

