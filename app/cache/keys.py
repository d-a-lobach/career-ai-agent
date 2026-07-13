class RedisKeys:

    @staticmethod
    def vacancy(user_id: int) -> str:
        return f"user:{user_id}:vacancy"

    @staticmethod
    def resume(user_id: int) -> str:
        return f"user:{user_id}:resume"

    @staticmethod
    def resume_id(user_id: int) -> str:
        return f"user:{user_id}:resume_id"

    @staticmethod
    def dialog(user_id: int) -> str:
        return f"user:{user_id}:dialog"