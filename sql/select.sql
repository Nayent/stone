SELECT
    TO_CHAR(trans.ref_date, 'Month') as Month,
    SUM(amount) as Amount
FROM transaction trans
JOIN transaction_type trans_type
    on trans.transaction_type_id = trans_type.id
WHERE DATE_TRUNC('year', ref_date) = DATE_TRUNC('year', CURRENT_DATE)
    AND trans_type.description = 'Pagamento de Boleto'
GROUP BY 1, ref_date
ORDER BY ref_date;