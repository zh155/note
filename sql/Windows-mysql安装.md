���뻷������

mysqld --initialize-insecure
���Զ��� D:\devtool\mysq\ �´���dataĿ¼�������ֹ�����dataĿ¼
mysqld -install
�ⲽ�ǰ�װ mysql ����, ������ǹ���Ա���л���ʾ ��Install/Remove of the Service Denied!�� 
, �����cd�� mysql��binĿ¼ ����װ��·��Ĭ���� C:\Program Files\MySQL\ , ���������ʧ�� ��ʾ ��
����ϵͳ���� 2�� ϵͳ�Ҳ���ָ�����ļ���
net start mysql
�ⲽ������mysql ���� ���û�е�һ�� �ⲽ������ʧ�� ����ʾ ������� NET HELPMSG 3534 �Ի�ø���İ�����
����mysql�Ժ�Ϳ��� ��cmd �� ���� mysql -u root -p ��ɳ��ε�½��
Ȼ�����root�˻�������Ϊ'root'
���update mysql.user set authentication_string=password("root") where user="root";
Ȼ������flush privileges;��ˢ���˻���Ϣ��