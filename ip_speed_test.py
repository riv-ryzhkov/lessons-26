import speedtest as st

def Speed_test():
    test = st.Speedtest()
    # print(*dir(test), sep='\n')

    # Получаем список серверов и выбираем ближайший
    servers = test.get_servers()
    # print(servers)
    # breakpoint()
    test.get_best_server(servers)

    # Тест на загрузку
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print('Download speed in Mbps =', down_speed)

    # Тест на отправку
    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print('Upload speed in Mbps =', up_speed)
    #
    # Пинг
    ping = test.results.ping
    print('Ping:', ping)

Speed_test()
