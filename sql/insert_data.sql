INSERT INTO transaction_type(description) VALUES
    ('Pagamento de Boleto'),
    ('Depósito'),
    ('Saque'),
    ('Transferência Recebida'),
    ('Transferência Realizada');


-----


INSERT INTO account(name, cpf, agency, account_number) VALUES
    ('TESTE1', '123', '00001', '18934-1'),
    ('TESTE2', '1234', '00001', '28934-1'),
    ('TESTE3', '1235', '00001', '38934-1'),
    ('TESTE4', '1236', '00001', '48934-1'),
    ('TESTE5', '1237', '00001', '58934-1'),
    ('TESTE6', '1238', '00001', '68934-1'),
    ('TESTE7', '1239', '00001', '78934-1'),
    ('TESTE8', '1230', '00001', '88934-1'),
    ('TESTE9', '1231', '00001', '98934-1'),
    ('TESTE10', '1232', '00001', '09934-1'),
    ('TESTE11', '1233', '00001', '19934-1');


-----


INSERT INTO transaction(amount, ref_date, external_agency, external_account_number, internal_account, transaction_type_id) VALUES
    (20700, '2022-01-01'::date, '00001', '1234567890', 1, 1),
    (21700, '2022-02-01'::date, '00001', '1234567890', 2, 1),
    (22700, '2022-03-01'::date, '00001', '1234567890', 1, 1),
    (23700, '2022-04-01'::date, '00001', '1234567890', 1, 1),
    (24700, '2022-05-01'::date, '00001', '1234567890', 1, 1),
    (25700, '2021-01-01'::date, '00001', '1234567890', 3, 1),
    (27700, '2023-01-01'::date, '00001', '1234567890', 1, 1),
    (26700, '2023-01-01'::date, '00001', '1234567890', 1, 2),
    (28700, '2022-10-01'::date, '00001', '1234567890', 1, 1),
    (28700, '2022-10-01'::date, '00001', '1234567890', 1, 1),
    (28700, '2022-10-01'::date, '00001', '1234567890', 1, 2);