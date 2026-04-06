import datetime


def gerar_data_hora(indice):
    base = datetime.datetime(2026, 3, 23, 14, 0, 0)
    incremento = datetime.timedelta(seconds=indice * 17)
    return (base + incremento).strftime('%d/%m/%Y %H:%M:%S')



def gerar_ip(indice):
    faixa = indice % 24

    if faixa >= 4 and faixa <= 6:
        return '10.0.0.50'
    if faixa >= 7 and faixa <= 8:
        return '203.0.113.10'
    if faixa >= 13 and faixa <= 15:
        return '198.51.100.20'
    if faixa >= 16 and faixa <= 20:
        return '172.16.0.9'
    if faixa == 21:
        return '203.0.113.80'
    if faixa == 22:
        return '192.168.0.44'
    if faixa == 23:
        return '203.0.113.81'

    numero = indice % 6
    if numero == 0:
        return '192.168.0.10'
    if numero == 1:
        return '192.168.0.11'
    if numero == 2:
        return '192.168.0.12'
    if numero == 3:
        return '192.168.0.13'
    if numero == 4:
        return '192.168.0.14'
    return '192.168.0.15'



def gerar_recurso(indice):
    faixa = indice % 24

    if faixa == 0:
        return '/home'
    if faixa == 1:
        return '/produtos'
    if faixa == 2:
        return '/carrinho'
    if faixa == 3:
        return '/checkout'
    if faixa >= 4 and faixa <= 6:
        return '/login'
    if faixa == 7:
        return '/admin'
    if faixa == 8:
        return '/admin'
    if faixa >= 9 and faixa <= 12:
        return '/produtos'
    if faixa >= 13 and faixa <= 15:
        return '/api/pedidos'
    if faixa == 16:
        return '/home'
    if faixa == 17:
        return '/produtos'
    if faixa == 18:
        return '/private'
    if faixa == 19:
        return '/home'
    if faixa == 20:
        return '/produtos'
    if faixa == 21:
        return '/backup'
    if faixa == 22:
        return '/pagina-inexistente'
    return '/config'



def gerar_metodo(recurso):
    if recurso == '/login':
        return 'POST'
    if recurso == '/checkout':
        return 'POST'
    if recurso == '/api/pedidos':
        return 'POST'
    return 'GET'



def gerar_status(indice, recurso):
    faixa = indice % 24

    if faixa >= 4 and faixa <= 6:
        return 403
    if faixa == 7:
        return 403
    if faixa == 8:
        return 404
    if faixa >= 13 and faixa <= 15:
        return 500
    if faixa == 21:
        return 403
    if faixa == 22:
        return 404
    if faixa == 23:
        return 403

    if recurso == '/pagina-inexistente':
        return 404

    return 200



def gerar_tempo_resposta(indice, status):
    faixa = indice % 24

    if faixa == 0:
        return 180
    if faixa == 1:
        return 260
    if faixa == 2:
        return 170
    if faixa == 3:
        return 250
    if faixa == 4:
        return 140
    if faixa == 5:
        return 160
    if faixa == 6:
        return 180
    if faixa == 7:
        return 170
    if faixa == 8:
        return 150
    if faixa == 9:
        return 120
    if faixa == 10:
        return 240
    if faixa == 11:
        return 390
    if faixa == 12:
        return 700
    if faixa == 13:
        return 300
    if faixa == 14:
        return 310
    if faixa == 15:
        return 290
    if faixa == 16:
        return 90
    if faixa == 17:
        return 95
    if faixa == 18:
        return 90
    if faixa == 19:
        return 95
    if faixa == 20:
        return 90
    if faixa == 21:
        return 400
    if faixa == 22:
        return 130
    if faixa == 23:
        return 210

    if status == 500:
        return 300
    if status == 404:
        return 130
    if status == 403:
        return 210
    return 200



def gerar_tamanho(status, recurso):
    if status == 500:
        return 128
    if status == 404:
        return 256
    if status == 403:
        return 196
    if recurso == '/produtos':
        return 2048
    if recurso == '/home':
        return 1024
    if recurso == '/carrinho':
        return 768
    if recurso == '/checkout':
        return 640
    if recurso == '/api/pedidos':
        return 512
    if recurso == '/private':
        return 220
    if recurso == '/backup':
        return 180
    if recurso == '/config':
        return 200
    return 700



def gerar_protocolo(indice):
    resto = indice % 3
    if resto == 0:
        return 'HTTP/1.0'
    if resto == 1:
        return 'HTTP/1.1'
    return 'HTTP/2'



def gerar_user_agent(indice):
    faixa = indice % 24

    if faixa == 16:
        return 'GoogleBot'
    if faixa == 17:
        return 'CrawlerX'
    if faixa == 18:
        return 'SpiderAuto'
    if faixa == 21:
        return 'BackupBot'
    if faixa == 23:
        return 'curl'

    resto = indice % 5
    if resto == 0:
        return 'Chrome'
    if resto == 1:
        return 'Firefox'
    if resto == 2:
        return 'Edge'
    if resto == 3:
        return 'Safari'
    return 'Postman'



def gerar_referer(recurso):
    if recurso == '/home':
        return '/landing'
    if recurso == '/produtos':
        return '/home'
    if recurso == '/carrinho':
        return '/produtos'
    if recurso == '/checkout':
        return '/carrinho'
    if recurso == '/login':
        return '/home'
    if recurso == '/admin':
        return '/login'
    if recurso == '/backup':
        return '/admin'
    if recurso == '/config':
        return '/admin'
    if recurso == '/private':
        return '/home'
    if recurso == '/api/pedidos':
        return '/checkout'
    return '/home'



def montar_log(indice):
    data_hora = gerar_data_hora(indice)
    recurso = gerar_recurso(indice)
    ip = gerar_ip(indice)
    metodo = gerar_metodo(recurso)
    status = gerar_status(indice, recurso)
    tempo = gerar_tempo_resposta(indice, status)
    tamanho = gerar_tamanho(status, recurso)
    protocolo = gerar_protocolo(indice)
    user_agent = gerar_user_agent(indice)
    referer = gerar_referer(recurso)

    return f'[{data_hora}] {ip} - {metodo} - {status} - {recurso} - {tempo}ms - {tamanho}B - {protocolo} - {user_agent} - {referer}'



def gerar_arquivo_logs(nome_arquivo, quantidade):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for indice in range(quantidade):
            arquivo.write(montar_log(indice) + '\n')

    print('Logs gerados com sucesso.')



def limpar_linha(linha):
    texto = ''
    i = 0

    while i < len(linha):
        if linha[i] != '\n' and linha[i] != '\r':
            texto += linha[i]
        i += 1

    return texto



def extrair_numeros(texto):
    numeros = ''
    i = 0

    while i < len(texto):
        if texto[i] >= '0' and texto[i] <= '9':
            numeros += texto[i]
        i += 1

    if numeros == '':
        return 0
    return int(numeros)



def extrair_data_hora(texto):
    if texto == '':
        return ''
    if texto[0] != '[':
        return ''

    i = 1
    data_hora = ''

    while i < len(texto) and texto[i] != ']':
        data_hora += texto[i]
        i += 1

    if i >= len(texto):
        return ''
    return data_hora



def obter_inicio_campos(texto):
    i = 0

    while i < len(texto) and texto[i] != ']':
        i += 1

    if i >= len(texto):
        return -1

    i += 1
    if i < len(texto) and texto[i] == ' ':
        i += 1

    return i



def obter_campo_por_ordem(texto, ordem):
    inicio = obter_inicio_campos(texto)
    if inicio == -1:
        return ''

    campo_atual = ''
    ordem_atual = 1
    i = inicio

    while i < len(texto):
        if i + 2 < len(texto):
            if texto[i] == ' ' and texto[i + 1] == '-' and texto[i + 2] == ' ':
                if ordem_atual == ordem:
                    return campo_atual
                campo_atual = ''
                ordem_atual += 1
                i += 3
                continue

        campo_atual += texto[i]
        i += 1

    if ordem_atual == ordem:
        return campo_atual
    return ''



def extrair_ip(texto):
    return obter_campo_por_ordem(texto, 1)



def extrair_metodo(texto):
    return obter_campo_por_ordem(texto, 2)



def extrair_status(texto):
    return extrair_numeros(obter_campo_por_ordem(texto, 3))



def extrair_recurso(texto):
    return obter_campo_por_ordem(texto, 4)



def extrair_tempo(texto):
    return extrair_numeros(obter_campo_por_ordem(texto, 5))



def extrair_tamanho(texto):
    return extrair_numeros(obter_campo_por_ordem(texto, 6))



def extrair_protocolo(texto):
    return obter_campo_por_ordem(texto, 7)



def extrair_user_agent(texto):
    return obter_campo_por_ordem(texto, 8)



def extrair_referer(texto):
    return obter_campo_por_ordem(texto, 9)



def linha_valida(texto):
    if extrair_data_hora(texto) == '':
        return False
    if extrair_ip(texto) == '':
        return False
    if extrair_metodo(texto) == '':
        return False
    if extrair_recurso(texto) == '':
        return False
    if extrair_protocolo(texto) == '':
        return False
    if extrair_user_agent(texto) == '':
        return False
    if extrair_referer(texto) == '':
        return False
    return True



def classificar_tempo(tempo):
    if tempo < 200:
        return 'rapido'
    if tempo <= 799:
        return 'normal'
    return 'lento'



def obter_recurso_mais_acessado(cont_home, cont_produtos, cont_carrinho, cont_checkout,
                                cont_login, cont_admin, cont_api_pedidos, cont_private,
                                cont_backup, cont_pagina_inexistente, cont_config):
    recurso_maior = '/home'
    maior = cont_home

    if cont_produtos > maior:
        maior = cont_produtos
        recurso_maior = '/produtos'
    if cont_carrinho > maior:
        maior = cont_carrinho
        recurso_maior = '/carrinho'
    if cont_checkout > maior:
        maior = cont_checkout
        recurso_maior = '/checkout'
    if cont_login > maior:
        maior = cont_login
        recurso_maior = '/login'
    if cont_admin > maior:
        maior = cont_admin
        recurso_maior = '/admin'
    if cont_api_pedidos > maior:
        maior = cont_api_pedidos
        recurso_maior = '/api/pedidos'
    if cont_private > maior:
        maior = cont_private
        recurso_maior = '/private'
    if cont_backup > maior:
        maior = cont_backup
        recurso_maior = '/backup'
    if cont_pagina_inexistente > maior:
        maior = cont_pagina_inexistente
        recurso_maior = '/pagina-inexistente'
    if cont_config > maior:
        recurso_maior = '/config'

    return recurso_maior



def obter_ip_mais_ativo(cont_ip_1, cont_ip_2, cont_ip_3, cont_ip_4, cont_ip_5, cont_ip_6,
                        cont_ip_7, cont_ip_8, cont_ip_9, cont_ip_10, cont_ip_11,
                        cont_ip_12, cont_ip_13):
    ip_maior = '192.168.0.10'
    maior = cont_ip_1

    if cont_ip_2 > maior:
        maior = cont_ip_2
        ip_maior = '192.168.0.11'
    if cont_ip_3 > maior:
        maior = cont_ip_3
        ip_maior = '192.168.0.12'
    if cont_ip_4 > maior:
        maior = cont_ip_4
        ip_maior = '192.168.0.13'
    if cont_ip_5 > maior:
        maior = cont_ip_5
        ip_maior = '192.168.0.14'
    if cont_ip_6 > maior:
        maior = cont_ip_6
        ip_maior = '192.168.0.15'
    if cont_ip_7 > maior:
        maior = cont_ip_7
        ip_maior = '10.0.0.50'
    if cont_ip_8 > maior:
        maior = cont_ip_8
        ip_maior = '203.0.113.10'
    if cont_ip_9 > maior:
        maior = cont_ip_9
        ip_maior = '198.51.100.20'
    if cont_ip_10 > maior:
        maior = cont_ip_10
        ip_maior = '172.16.0.9'
    if cont_ip_11 > maior:
        maior = cont_ip_11
        ip_maior = '203.0.113.80'
    if cont_ip_12 > maior:
        maior = cont_ip_12
        ip_maior = '192.168.0.44'
    if cont_ip_13 > maior:
        ip_maior = '203.0.113.81'

    return ip_maior



def classificar_estado_final(disponibilidade, acessos_lentos, total_acessos, falhas_criticas, suspeitas_bot):
    if falhas_criticas >= 1 or disponibilidade < 70:
        return 'CRÍTICO'
    if disponibilidade < 85 or acessos_lentos >= (total_acessos / 3):
        return 'INSTÁVEL'
    if disponibilidade < 95 or suspeitas_bot > 0:
        return 'ATENÇÃO'
    return 'SAUDÁVEL'



def montar_texto_relatorio(total_acessos, total_sucessos, total_erros, total_erros_criticos,
                           disponibilidade, taxa_erro, tempo_medio, maior_tempo, menor_tempo,
                           acessos_rapidos, acessos_normais, acessos_lentos,
                           status_200, status_403, status_404, status_500,
                           recurso_mais_acessado, ip_mais_ativo, ip_com_mais_erros,
                           eventos_forca_bruta, ultimo_ip_forca_bruta,
                           acessos_indevidos_admin, eventos_degradacao,
                           eventos_falha_critica, suspeitas_bot, ultimo_ip_bot,
                           acessos_rotas_sensiveis, falhas_rotas_sensiveis, estado_final):
    texto = ''
    texto += '\nRELATORIO FINAL\n'
    texto += 'Total de acessos: ' + str(total_acessos) + '\n'
    texto += 'Total de sucessos: ' + str(total_sucessos) + '\n'
    texto += 'Total de erros: ' + str(total_erros) + '\n'
    texto += 'Total de erros criticos: ' + str(total_erros_criticos) + '\n'
    texto += 'Disponibilidade do sistema: ' + f'{disponibilidade:.2f}%' + '\n'
    texto += 'Taxa de erro: ' + f'{taxa_erro:.2f}%' + '\n'
    texto += 'Tempo medio de resposta: ' + f'{tempo_medio:.2f} ms' + '\n'
    texto += 'Maior tempo de resposta: ' + str(maior_tempo) + ' ms\n'
    texto += 'Menor tempo de resposta: ' + str(menor_tempo) + ' ms\n'
    texto += 'Quantidade de acessos rapidos: ' + str(acessos_rapidos) + '\n'
    texto += 'Quantidade de acessos normais: ' + str(acessos_normais) + '\n'
    texto += 'Quantidade de acessos lentos: ' + str(acessos_lentos) + '\n'
    texto += 'Quantidade de status 200: ' + str(status_200) + '\n'
    texto += 'Quantidade de status 403: ' + str(status_403) + '\n'
    texto += 'Quantidade de status 404: ' + str(status_404) + '\n'
    texto += 'Quantidade de status 500: ' + str(status_500) + '\n'
    texto += 'Recurso mais acessado: ' + recurso_mais_acessado + '\n'
    texto += 'IP mais ativo: ' + ip_mais_ativo + '\n'
    texto += 'IP com mais erros: ' + ip_com_mais_erros + '\n'
    texto += 'Total de eventos de forca bruta: ' + str(eventos_forca_bruta) + '\n'
    texto += 'Ultimo IP com forca bruta detectada: ' + ultimo_ip_forca_bruta + '\n'
    texto += 'Total de acessos indevidos ao /admin: ' + str(acessos_indevidos_admin) + '\n'
    texto += 'Total de eventos de degradacao de desempenho: ' + str(eventos_degradacao) + '\n'
    texto += 'Total de eventos de falha critica: ' + str(eventos_falha_critica) + '\n'
    texto += 'Total de suspeitas de bot: ' + str(suspeitas_bot) + '\n'
    texto += 'Ultimo IP suspeito de bot: ' + ultimo_ip_bot + '\n'
    texto += 'Total de acessos a rotas sensiveis: ' + str(acessos_rotas_sensiveis) + '\n'
    texto += 'Total de falhas em rotas sensiveis: ' + str(falhas_rotas_sensiveis) + '\n'
    texto += 'Estado final do sistema: ' + estado_final
    return texto



def imprimir_relatorio(texto_relatorio):
    print(texto_relatorio)



def analisar_arquivo_logs(nome_arquivo):
    total_acessos = 0
    total_sucessos = 0
    total_erros = 0
    total_erros_criticos = 0
    soma_tempo = 0
    maior_tempo = 0
    menor_tempo = 0
    acessos_rapidos = 0
    acessos_normais = 0
    acessos_lentos = 0
    status_200 = 0
    status_403 = 0
    status_404 = 0
    status_500 = 0
    acessos_indevidos_admin = 0
    eventos_forca_bruta = 0
    ultimo_ip_forca_bruta = 'N/A'
    eventos_degradacao = 0
    eventos_falha_critica = 0
    suspeitas_bot = 0
    ultimo_ip_bot = 'N/A'
    acessos_rotas_sensiveis = 0
    falhas_rotas_sensiveis = 0

    cont_home = 0
    cont_produtos = 0
    cont_carrinho = 0
    cont_checkout = 0
    cont_login = 0
    cont_admin = 0
    cont_api_pedidos = 0
    cont_private = 0
    cont_backup = 0
    cont_pagina_inexistente = 0
    cont_config = 0

    cont_ip_1 = 0
    cont_ip_2 = 0
    cont_ip_3 = 0
    cont_ip_4 = 0
    cont_ip_5 = 0
    cont_ip_6 = 0
    cont_ip_7 = 0
    cont_ip_8 = 0
    cont_ip_9 = 0
    cont_ip_10 = 0
    cont_ip_11 = 0
    cont_ip_12 = 0
    cont_ip_13 = 0

    cont_ip_erro_1 = 0
    cont_ip_erro_2 = 0
    cont_ip_erro_3 = 0
    cont_ip_erro_4 = 0
    cont_ip_erro_5 = 0
    cont_ip_erro_6 = 0
    cont_ip_erro_7 = 0
    cont_ip_erro_8 = 0
    cont_ip_erro_9 = 0
    cont_ip_erro_10 = 0
    cont_ip_erro_11 = 0
    cont_ip_erro_12 = 0
    cont_ip_erro_13 = 0

    ultimo_ip_login_403 = ''
    sequencia_login_403 = 0
    evento_forca_ativo = False

    tempo_anterior = -1
    aumentos_consecutivos = 0
    evento_degradacao_ativo = False

    erros_500_consecutivos = 0
    evento_falha_ativo = False

    ultimo_ip_sequencia = ''
    sequencia_mesmo_ip = 0
    evento_bot_ip_ativo = False

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            texto = limpar_linha(linha)

            if texto == '':
                continue
            if linha_valida(texto) is False:
                continue

            total_acessos += 1

            ip = extrair_ip(texto)
            status = extrair_status(texto)
            recurso = extrair_recurso(texto)
            tempo = extrair_tempo(texto)
            user_agent = extrair_user_agent(texto)

            if recurso == '/home':
                cont_home += 1
            elif recurso == '/produtos':
                cont_produtos += 1
            elif recurso == '/carrinho':
                cont_carrinho += 1
            elif recurso == '/checkout':
                cont_checkout += 1
            elif recurso == '/login':
                cont_login += 1
            elif recurso == '/admin':
                cont_admin += 1
            elif recurso == '/api/pedidos':
                cont_api_pedidos += 1
            elif recurso == '/private':
                cont_private += 1
            elif recurso == '/backup':
                cont_backup += 1
            elif recurso == '/pagina-inexistente':
                cont_pagina_inexistente += 1
            elif recurso == '/config':
                cont_config += 1

            if ip == '192.168.0.10':
                cont_ip_1 += 1
            elif ip == '192.168.0.11':
                cont_ip_2 += 1
            elif ip == '192.168.0.12':
                cont_ip_3 += 1
            elif ip == '192.168.0.13':
                cont_ip_4 += 1
            elif ip == '192.168.0.14':
                cont_ip_5 += 1
            elif ip == '192.168.0.15':
                cont_ip_6 += 1
            elif ip == '10.0.0.50':
                cont_ip_7 += 1
            elif ip == '203.0.113.10':
                cont_ip_8 += 1
            elif ip == '198.51.100.20':
                cont_ip_9 += 1
            elif ip == '172.16.0.9':
                cont_ip_10 += 1
            elif ip == '203.0.113.80':
                cont_ip_11 += 1
            elif ip == '192.168.0.44':
                cont_ip_12 += 1
            elif ip == '203.0.113.81':
                cont_ip_13 += 1

            if status == 200:
                total_sucessos += 1
                status_200 += 1
            else:
                total_erros += 1

                if ip == '192.168.0.10':
                    cont_ip_erro_1 += 1
                elif ip == '192.168.0.11':
                    cont_ip_erro_2 += 1
                elif ip == '192.168.0.12':
                    cont_ip_erro_3 += 1
                elif ip == '192.168.0.13':
                    cont_ip_erro_4 += 1
                elif ip == '192.168.0.14':
                    cont_ip_erro_5 += 1
                elif ip == '192.168.0.15':
                    cont_ip_erro_6 += 1
                elif ip == '10.0.0.50':
                    cont_ip_erro_7 += 1
                elif ip == '203.0.113.10':
                    cont_ip_erro_8 += 1
                elif ip == '198.51.100.20':
                    cont_ip_erro_9 += 1
                elif ip == '172.16.0.9':
                    cont_ip_erro_10 += 1
                elif ip == '203.0.113.80':
                    cont_ip_erro_11 += 1
                elif ip == '192.168.0.44':
                    cont_ip_erro_12 += 1
                elif ip == '203.0.113.81':
                    cont_ip_erro_13 += 1

                if status == 403:
                    status_403 += 1
                if status == 404:
                    status_404 += 1
                if status == 500:
                    status_500 += 1
                    total_erros_criticos += 1

            soma_tempo += tempo

            if total_acessos == 1:
                maior_tempo = tempo
                menor_tempo = tempo
            else:
                if tempo > maior_tempo:
                    maior_tempo = tempo
                if tempo < menor_tempo:
                    menor_tempo = tempo

            classificacao_tempo = classificar_tempo(tempo)
            if classificacao_tempo == 'rapido':
                acessos_rapidos += 1
            elif classificacao_tempo == 'normal':
                acessos_normais += 1
            else:
                acessos_lentos += 1

            if recurso == '/admin' and status != 200:
                acessos_indevidos_admin += 1

            if recurso == '/admin' or recurso == '/backup' or recurso == '/config' or recurso == '/private':
                acessos_rotas_sensiveis += 1
                if status != 200:
                    falhas_rotas_sensiveis += 1

            if recurso == '/login' and status == 403:
                if ip == ultimo_ip_login_403:
                    sequencia_login_403 += 1
                else:
                    ultimo_ip_login_403 = ip
                    sequencia_login_403 = 1
                    evento_forca_ativo = False

                if sequencia_login_403 >= 3 and evento_forca_ativo is False:
                    eventos_forca_bruta += 1
                    ultimo_ip_forca_bruta = ip
                    evento_forca_ativo = True
            else:
                ultimo_ip_login_403 = ''
                sequencia_login_403 = 0
                evento_forca_ativo = False

            if tempo_anterior != -1 and tempo > tempo_anterior:
                aumentos_consecutivos += 1
            else:
                aumentos_consecutivos = 0
                evento_degradacao_ativo = False

            if aumentos_consecutivos >= 3 and evento_degradacao_ativo is False:
                eventos_degradacao += 1
                evento_degradacao_ativo = True

            tempo_anterior = tempo

            if status == 500:
                erros_500_consecutivos += 1
                if erros_500_consecutivos >= 3 and evento_falha_ativo is False:
                    eventos_falha_critica += 1
                    evento_falha_ativo = True
            else:
                erros_500_consecutivos = 0
                evento_falha_ativo = False

            if 'Bot' in user_agent or 'Crawler' in user_agent or 'Spider' in user_agent:
                suspeitas_bot += 1
                ultimo_ip_bot = ip

            if ip == ultimo_ip_sequencia:
                sequencia_mesmo_ip += 1
            else:
                ultimo_ip_sequencia = ip
                sequencia_mesmo_ip = 1
                evento_bot_ip_ativo = False

            if sequencia_mesmo_ip >= 5 and evento_bot_ip_ativo is False:
                suspeitas_bot += 1
                ultimo_ip_bot = ip
                evento_bot_ip_ativo = True

    if total_acessos > 0:
        disponibilidade = (total_sucessos / total_acessos) * 100
        taxa_erro = (total_erros / total_acessos) * 100
        tempo_medio = soma_tempo / total_acessos
    else:
        disponibilidade = 0
        taxa_erro = 0
        tempo_medio = 0

    recurso_mais_acessado = obter_recurso_mais_acessado(
        cont_home, cont_produtos, cont_carrinho, cont_checkout,
        cont_login, cont_admin, cont_api_pedidos, cont_private,
        cont_backup, cont_pagina_inexistente, cont_config
    )

    ip_mais_ativo = obter_ip_mais_ativo(
        cont_ip_1, cont_ip_2, cont_ip_3, cont_ip_4, cont_ip_5, cont_ip_6,
        cont_ip_7, cont_ip_8, cont_ip_9, cont_ip_10, cont_ip_11,
        cont_ip_12, cont_ip_13
    )

    ip_com_mais_erros = obter_ip_mais_ativo(
        cont_ip_erro_1, cont_ip_erro_2, cont_ip_erro_3, cont_ip_erro_4,
        cont_ip_erro_5, cont_ip_erro_6, cont_ip_erro_7, cont_ip_erro_8,
        cont_ip_erro_9, cont_ip_erro_10, cont_ip_erro_11, cont_ip_erro_12,
        cont_ip_erro_13
    )

    estado_final = classificar_estado_final(
        disponibilidade,
        acessos_lentos,
        total_acessos,
        eventos_falha_critica,
        suspeitas_bot
    )

    texto_relatorio = montar_texto_relatorio(
        total_acessos, total_sucessos, total_erros, total_erros_criticos,
        disponibilidade, taxa_erro, tempo_medio, maior_tempo, menor_tempo,
        acessos_rapidos, acessos_normais, acessos_lentos,
        status_200, status_403, status_404, status_500,
        recurso_mais_acessado, ip_mais_ativo, ip_com_mais_erros,
        eventos_forca_bruta, ultimo_ip_forca_bruta,
        acessos_indevidos_admin, eventos_degradacao,
        eventos_falha_critica, suspeitas_bot, ultimo_ip_bot,
        acessos_rotas_sensiveis, falhas_rotas_sensiveis, estado_final
    )

    imprimir_relatorio(texto_relatorio)
    return texto_relatorio



def menu():
    nome_arquivo = 'log.txt'

    while True:
        print('\nMONITOR LOGPY')
        print('1. Gerar logs')
        print('2. Analisar logs')
        print('3. Gerar e analisar')
        print('4. Sair')

        opcao = input('Digite a opcao desejada: ')

        if opcao == '1':
            try:
                quantidade = int(input('Digite a quantidade de logs: '))
                if quantidade <= 0:
                    print('Digite um numero maior que zero.')
                else:
                    gerar_arquivo_logs(nome_arquivo, quantidade)
            except ValueError:
                print('Entrada invalida.')

        elif opcao == '2':
            try:
                analisar_arquivo_logs(nome_arquivo)
            except FileNotFoundError:
                print('Arquivo de log nao encontrado.')

        elif opcao == '3':
            try:
                quantidade = int(input('Digite a quantidade de logs: '))
                if quantidade <= 0:
                    print('Digite um numero maior que zero.')
                else:
                    gerar_arquivo_logs(nome_arquivo, quantidade)
                    analisar_arquivo_logs(nome_arquivo)
            except ValueError:
                print('Entrada invalida.')

        elif opcao == '4':
            print('Encerrando o sistema.')
            break

        else:
            print('Opcao invalida.')


menu()
