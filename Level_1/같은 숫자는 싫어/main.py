def no_continuous(s):
    # 함수를 완성하세요
    result = []
    cmp = ""
    for c in list(s):
        if cmp != c:
            result.append(c)
            cmp = c
    return result

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))