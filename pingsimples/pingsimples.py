import os


ip_ou_host = input("Digite o IP ou host:")

os.system('ping -n 6 {}'.format(ip_ou_host))
