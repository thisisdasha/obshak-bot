create table obshak(
    id integer primary key,
    creditor_id text key,
    debtor_id text key,
    amount integer,
    created datetime DEFAULT CURRENT_TIMESTAMP
);
