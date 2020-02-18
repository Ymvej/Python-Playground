dégats = 10000
franchise = 0
remboursement = 0

franchise = dégats * 10 / 100 #10

if franchise >= 15 and franchise <=500:
    remboursement = dégats - franchise
    print("L'assurance vous rembourse",remboursement,"€. La franchise s'élève à",franchise,"€.")
elif franchise <= 15:
    franchise = 15
    remboursement = dégats - franchise
    print("L'assurance vous rembourse",remboursement,"€. La franchise s'élève à",franchise,"€.")
elif franchise >= 500:
    franchise = 500
    remboursement = dégats - franchise
    print("L'assurance vous rembourse",remboursement,"€. La franchise s'élève à",franchise,"€.")
else:
    print("Y'a rien qui va.")