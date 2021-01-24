
def test_find_last_status_for_code(prepare_data):
    """Находим последние статусы по каждому коду"""
    con, expected_result = prepare_data
    cur = con.cursor()
    cur.execute(
        """WITH query_in (code, status, created, last)
            AS (
                SELECT code.id, status.status, status.created,
                MAX(status.created) OVER(PARTITION BY code) AS last
                FROM code INNER JOIN STATUS
                ON code.id = status.code_id)
    
            SELECT code, status, created
            FROM query_in
            WHERE created = last"""
    )

    received_result = cur.fetchall()
    assert received_result == expected_result, f"Expected {expected_result} \n got {received_result} "

