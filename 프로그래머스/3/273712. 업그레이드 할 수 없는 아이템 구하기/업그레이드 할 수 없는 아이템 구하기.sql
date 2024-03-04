-- 코드를 작성해주세요
SELECT INFO.ITEM_ID, INFO.ITEM_NAME, INFO.RARITY FROM ITEM_INFO AS INFO
LEFT JOIN ITEM_TREE AS TREE
ON INFO.ITEM_ID = TREE.PARENT_ITEM_ID
WHERE TREE.PARENT_ITEM_ID IS NULL
ORDER BY INFO.ITEM_ID DESC;