-- 코드를 입력하세요
WITH NEW_JULY AS
(
    SELECT SHIPMENT_ID, FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER FROM JULY 
    GROUP BY FLAVOR
)

SELECT FH.FLAVOR AS FLAVOR
FROM FIRST_HALF AS FH
JOIN NEW_JULY
USING (SHIPMENT_ID)
ORDER BY (FH.TOTAL_ORDER + NEW_JULY.TOTAL_ORDER) DESC
LIMIT 3;