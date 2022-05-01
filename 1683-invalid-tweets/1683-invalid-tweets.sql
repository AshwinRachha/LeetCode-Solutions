# Write your MySQL query statement below
SELECT tweet_id FROM TWEETS
WHERE CHAR_LENGTH(TWEETS.content) > 15;