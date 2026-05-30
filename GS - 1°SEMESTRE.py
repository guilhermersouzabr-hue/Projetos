# LINK VÍDEO: https://1drv.ms/v/c/7d5cbf8382d8ca5d/IQAaT5dC4l3NRaq5QKe46uXEAdiwkhG11nHvOUD8lSJVp-A?e=wdDdbN
# GRUPO: GUILHERME RODRIGUES DE SOUZA (RM:573803), PEDRO HENRIQUE NASCIMENTO SANTOS (RM:572420), GABRIEL VIANA BENTO (RM:572988)

print(f"\n---SPACE MODULE MONITORING SYSTEM---")
while True:
    quantidade_ciclos = int(input("Quantos ciclos de leitura deseja realizar?: "))
    if quantidade_ciclos < 3:
        print("A quantidade de ciclos deve ser no mínimo 3! Tente novamente")
    else:
        break

total_critico=0
mensagem_alerta=""

soma_vibracao=0
soma_temp=0
soma_latencia=0
soma_cpu=0
total_leituras_sensores=0

max_vibracao=0
min_vibracao=0
max_temp=0
min_temp=0
max_latencia=0
min_latencia=0
max_cpu=0
min_cpu=0

ciclo_atual=1
while ciclo_atual<=quantidade_ciclos:
    print(f"\n---LEITURA DE DADOS CICLO {ciclo_atual}---")
    sensor=1
    while sensor <= 5:
        print(f"\nLeitura de dados do Sensor {sensor}")

        vibracao=float(input(f"Digite a Vibração (g): "))
        if vibracao > 5 or vibracao < -5:
            total_critico+=1
            mensagem_alerta+=f"ALERTA: Vibração crítica de {vibracao}g detectada no ponto S{sensor} (Ciclo {ciclo_atual})\n"
        if ciclo_atual==1 and sensor==1:
            max_vibracao=vibracao
            min_vibracao=vibracao
        else:
            if vibracao>max_vibracao:
                max_vibracao=vibracao
            if vibracao<min_vibracao:
                min_vibracao=vibracao
        soma_vibracao+=vibracao

        temp = float(input(f"\nDigite a Temperatura (°C): "))
        if temp > 120 or temp < -150:
            total_critico += 1
            mensagem_alerta +=f"ALERTA: Temperatura crítica de {temp}°C detectada no ponto S{sensor} (Ciclo {ciclo_atual})\n"
        if ciclo_atual == 1 and sensor == 1:
            max_temp = temp
            min_temp = temp
        else:
            if temp > max_temp:
                max_temp = temp
            if temp < min_temp:
                min_temp = temp
        soma_temp+=temp

        latencia = int(input(f"\nDigite a Latência (ms): "))
        if latencia > 800:
            total_critico += 1
            mensagem_alerta += f"ALERTA: Latência crítica de {latencia}ms detectada no ponto S{sensor} (Ciclo {ciclo_atual})\n"
        if ciclo_atual == 1 and sensor == 1:
            max_latencia = latencia
            min_latencia = latencia
        else:
            if latencia > max_latencia:
                max_latencia = latencia
            if latencia < min_latencia:
                min_latencia = latencia
        soma_latencia += latencia

        sensor+=1
        total_leituras_sensores+=1

    cpu=float(input("\nQual o uso do CPU do computador de bordo (%): "))
    if cpu > 85:
        total_critico += 1
        mensagem_alerta += f"ALERTA: CPU crítica de {cpu}% detectada no Ciclo {ciclo_atual}\n"
    if ciclo_atual == 1:
        max_cpu = cpu
        min_cpu = cpu
    else:
        if cpu > max_cpu:
            max_cpu = cpu
        if cpu < min_cpu:
            min_cpu = cpu
    soma_cpu+=cpu

    ciclo_atual+=1

media_vibracao=soma_vibracao/total_leituras_sensores
media_temp=soma_temp/total_leituras_sensores
media_latencia=soma_latencia/total_leituras_sensores
media_cpu=soma_cpu/quantidade_ciclos

total_geral_dados = (total_leituras_sensores*3)+quantidade_ciclos
porcentagem_critica=(total_critico/total_geral_dados)*100

status=""
if porcentagem_critica < 10:
    status = "NORMAL -  Módulo operando dentro dos limites de segurança!"
elif porcentagem_critica <= 30:
    status = "ATENÇÃO - Monitoramento intensificado recomendado!"
else:
    status = "RISCO ELEVADO - Acionar protocolo de emergência!"

print("\n=====RELATÓRIO FINAL DETALHADO=====")
if mensagem_alerta != "":
    print(f"\n{mensagem_alerta}")
else:
    print("\nNenhum alerta crítico encontrado!")

print(f"Vibração -> Média: {media_vibracao:.2f}g | Máximo: {max_vibracao:.2f}g | Mínimo: {min_vibracao:.2f}g")
print(f"Temperatura -> Média: {media_temp:.2f}°C | Máximo: {max_temp:.2f}°C | Mínimo: {min_temp:.2f}°C")
print(f"Latência -> Média: {media_latencia:.2f}ms | Máximo: {max_latencia:.2f}ms | Mínimo: {min_latencia:.2f}ms")
print(f"CPU -> Média: {media_cpu:.2f}% | Máximo: {max_cpu:.2f}% | Mínimo: {min_cpu:.2f}%")

print(f"\nESTADO GERAL: {status}")

