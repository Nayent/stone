CREATE SEQUENCE account_id_seq;

CREATE TABLE account (
    id INTEGER PRIMARY KEY DEFAULT nextval('account_id_seq'),
    name VARCHAR(80) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    agency VARCHAR(5) NOT NULL,
    account_number VARCHAR(7) NOT NULL
);

CREATE INDEX agency_account_number ON account (agency, account_number);
CREATE INDEX account_cpf ON account (cpf);

ALTER TABLE account
ADD CONSTRAINT cpf_unique UNIQUE (cpf);

-----

CREATE SEQUENCE transaction_type_id_seq;

CREATE TABLE transaction_type (
    id INTEGER PRIMARY KEY DEFAULT nextval('transaction_type_id_seq'),
    description VARCHAR(30) NOT NULL
);

-----

CREATE SEQUENCE transaction_id_seq;

CREATE TABLE transaction (
    id INTEGER PRIMARY KEY DEFAULT nextval('transaction_id_seq'),
    amount INTEGER NOT NULL,
    ref_date TIMESTAMP NOT NULL,
    external_agency VARCHAR(5),
    external_account_number VARCHAR(10),
    internal_account_id INTEGER NOT NULL,
    transaction_type_id INTEGER NOT NULL,
    CONSTRAINT internal_account_id
        FOREIGN KEY(internal_account_id)
            REFERENCES account(id),
    CONSTRAINT transaction_type_id
        FOREIGN KEY(transaction_type_id)
            REFERENCES transaction_type(id)
);


CREATE INDEX transaction_ref_date ON transaction (ref_date);
CREATE INDEX id_account ON transaction (internal_account_id);