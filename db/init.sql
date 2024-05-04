
CREATE TABLE IF NOT EXISTS bank (
    id           int PRIMARY KEY,
    document_id  char(8), -- foreign key -> nombre, apellido, domicilio
    account      char(20) NOT NULL UNIQUE, 
    t_balance    decimal(4,2) DEFAULT 0.00::money,
    active       boolean DEFAULT false,
    last_update  timestamp
);

CREATE TABLE IF NOT EXISTS card (
    id           uuid PRIMARY KEY,
    id_student   text,
    document_id  char(8), --foreign key -> nos dara balance, dni
    expirate     date,
    active       boolean DEFAULT false,
    balance      decimal(4,2) DEFAULT 0.00,
    FOREIGN KEY(bank_account)
    REFERENCES bank(account) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS driver (
    id           uuid PRIMARY KEY,
    id_plate     text, -- foreign key -> info sobre el carro y empresa propietaria
    user         char(8), -- dni
    password     text NOT NULL,
    bank_account char(20), -- foreign key -> balance, dni
    FOREIGN KEY(bank_account)
    REFERENCES bank(account) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS payment (
    id          text PRIMARY KEY,
    id_card     uuid, -- foreign key
    id_driver   uuid, -- foreign key
    value       money NOT NULL,
    pay_date    timestamp NOT NULL,
    FOREIGN KEY (id_card)
    REFERENCES card(id) ON DELETE RESTRICT,
    FOREIGN KEY (id_driver)
    REFERENCES driver(id) ON DELETE RESTRICT
)