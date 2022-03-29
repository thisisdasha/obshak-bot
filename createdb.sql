create table obshak(
    creditor_id integer not null,
    debtor_id integer not null,
    amount integer,
    created_time datetime,
    raw_text text,
    PRIMARY KEY (creditor_id, debtor_id, created_time)
);
