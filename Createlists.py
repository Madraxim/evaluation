import gspread


creds = {
  "type": "service_account",
  "project_id": "tests-341815",
  "private_key_id": "532bb6434285686b422ba26db3a11d8f3750c7df",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDN6BPOHcDNfJTd\n5r8JBa9SkPwn1lf5bhDJBKQzlOrie2PacBTXisucUpHh+/YMD7bHw4jATAsCjDFI\nVqySrBYn7+RgGuEX8GAnPETUHJpDfI5RI3AfSmlYOgaXF7x+f7IIvzYzGwYoavMV\nvAYrk68IjnaQGKQ7KMyNCDDPzorzu18OqHrPUO0fnxYVcavSj+T1o/GAqYlSf1pT\nQeHGS2iwUYyWIj16PmQS1PeAx705CcZr3igNmvntOE/b3rwTFYxpGjlnj25FYkWA\nYJCJEAhN+McJXwO4Q5F4s5Sy8ygKA0xYEoYNQATDPExoeEoHD+Esw2LoW6v5lCwa\nu/5YqSC9AgMBAAECggEASsdjEfMaR0ZcZi5b6LHo10qSWQFuF8cST37hB16o4zG+\ntOEJoLHmelI+atzvobe/QNNRgczcHsO9TjE0IVxf+4cS4JhCcUg6E2W+9W2h1KqS\noQMGwEZs9b61EABt018a0DRpQawp01nsCFOtxfuvkKL0iiZ41oddqkZ0O7QeIJ+f\nOphaamxUn+79QLMW25Xf6VfHIRDNoUDW18WCPsJyHb5+q90sJi0eYqbtFvXk4AA9\nymBSvqhzN1kUhTyFbUg8X5C85hJMjCW7Qc10zE2QAWRSo9Q8frbPmpTIxjvE9ThA\nUMkXcVJTqJ1nUmbPRKVPOE72X+ss9Usg0XOwrjK9/QKBgQD9GzVzqqDFi8IlQaQa\nL/Lb69Np7ATLyMh6bFlhLK0pNIVcbmkZSrjr/7/Qn99dqsydILfL5jBccigU0Vaw\ngQVDOsrBkNlGhv7+iMCn9mZzvsnaVqQ48+ME1nJvL54vWz9wW674zo4EYvphW0eB\nUyYHd8xdO1tDDIefcdvMrX2B9wKBgQDQQrl1BEiQgkKHGcbiLbNAZXfweS8/Kraw\n0+ucUKSd5Xpf6EPvSNv46RwlXPoDvqvXXA6Lk6PF6gR/Vl7X2QjK8Q3+BR70Hx93\nzcmXefPNmRt/yyWSmb+YawIdCYbdob+NHOOAOdNNQmuLQxNyEf0a1nIoly7NGdXg\nUrzIyh8F6wKBgCH0fH8/7MGTtj/5RmKc/B+0y2/yUdJk5UBHONZof/J/MUTtKvxR\noe1HKhx61iRivYB22zFneCVuyyG/07lqFaKnSHwfSobDpYHQJshhrezpM3svFGjv\njw0fF8sCwF3qB+Cy7A5E55h/Dsfwzu7ykK9/ytLXG68rBybEx4/11liRAoGAVatM\n/OzhKMjcsxSQcpQYC6Jx3zMKk3JvqnfSkP+/Z9BxMaiq4XDYRCEoWdpQYl/58mJE\n/XejRBPK+9K8uw/lhQ36Eodqv0NaP38gsTYSa33TCRO5BgBHB1zlhqpXly4lTNgY\nYbPnzv1GngfepOrvci3K0hW2w9of1+JRFEvIzTcCgYEAiYXbd08LcQWJHgFGoEQb\n3iN2fI3N/SrkVayoCWnA8leMZ+2bS134qkFavEt7NEuHt2DoFsMEjAnMhgmyW4NM\neVr9fgB8vRdfxhkjfDOjN8exQ/OtrPYW6LzE6pK/G1/74oZfPGkAAAzpN+DoPTu0\nAyt68czwAKGnLT3qZUQ3sBo=\n-----END PRIVATE KEY-----\n",
  "client_email": "account@tests-341815.iam.gserviceaccount.com",
  "client_id": "100817940736117339505",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/account%40tests-341815.iam.gserviceaccount.com"
}



gc = gspread.service_account_from_dict(creds)

sh = gc.open('testspython')
worksheet = sh.worksheet("coworkers")
coworkers = worksheet.col_values(1)
worksheet_list = [i.title for i in sh.worksheets()]
print(worksheet_list)

for coworker in coworkers[1::]:
    if coworker not in worksheet_list[1::]:
        worksheet = sh.add_worksheet(title=coworker, rows="100", cols="15")
        print(f'{coworker} Создана')
        worksheet.append_row(['TG_ID', "Имя", "Фамилия", "Время", 'ВЕЖЛИВОСТЬ', 'СКОРОСТЬ', 'ЗНАНИЯ', 'ЧИСТОТА', 'КОММЕНТАРИЙ'])

    else:
        print(f'{coworker} уже существует в таблице')
