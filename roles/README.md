* Monitoring
  * [ansible-prometheus](https://github.com/devi1/ansible/tree/master/roles/ansible-prometheus) - основа системы мониторинга. Time Series Database, которая опрашивает сервисы, хранит в себе метрики и отдает их по запросу
  * [ansible-grafana](https://github.com/devi1/ansible/tree/master/roles/ansible-grafana) - фронтенд системы мониторинга. В удобном виде показывает метрики в веб-интерфейсе. Метрики запрашиваются у Prometheus  
  * [ansible-alertmanager](https://github.com/devi1/ansible/tree/master/roles/ansible-alertmanager) - Менеджер оповещений. Штатная система оповещений для Prometheus
  * [ansible-alertmanager-bot](https://github.com/devi1/ansible/tree/master/roles/ansible-alertmanager-bot) - Telegram бот для отправки алертов из Alertmanager
  * [ansible-blackbox-exporter](https://github.com/devi1/ansible/tree/master/roles/ansible-blackbox-exporter) - опрос сервисов по ICMP, TCP, HTTP и т.д. Опрашивает указанные сервисы и передает данные в prometheus
  * [ansible-node-exporter](https://github.com/devi1/ansible/tree/master/roles/ansible-node-exporter) - экспортер метрик с Linux систем. Передает данные в prometheus
  * [ansible-snmp-exporter](https://github.com/devi1/ansible/tree/master/roles/ansible-snmp-exporter) - опрашивает сетевые устройства по SNMP. Данные передает в prometheus
  * [ansible-mikrotik-exporter](https://github.com/devi1/ansible/tree/master/roles/ansible-mikrotik-exporter) - опрашивает RouterOS по API и отдает данные Prometheus'у. В нашей конфигурации данные передаются по шифрованному TLS каналу
  * [ansible-grok-exporter](https://github.com/devi1/ansible/tree/master/roles/ansible-grok-exporter) - Читает логи, парсит нужные данные и экспортирует в prometheus-читаемом виде. Применяется для мониторинга состояния медиаплееров, показывающих курсы валют

  Каждая роль подробно описана в своем каталоге