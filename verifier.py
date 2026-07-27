# v0.2.17
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *

class FactChecker(gl.Contract):
    last_claim: str
    last_verdict: str
    total_verifications: u256

    def __init__(self):
        self.last_claim = ""
        self.last_verdict = "NONE"
        self.total_verifications = u256(0)

    @gl.public.write
    def verify_claim(self, claim_text: str) -> str:
        prompt = f"""
        You are a factual verification consensus node on GenLayer.
        Analyze the following claim or news statement for factual plausibility:
        Claim: "{claim_text}"

        Respond strictly in JSON format with two keys:
        - "verdict": either "REAL", "FAKE", or "UNVERIFIED"
        - "reason": a brief 1-sentence explanation of why.
        """
        
        # Trigger GenLayer consensus engine across LLM nodes
        res = gl.exec_prompt(prompt)
        
        self.last_claim = claim_text
        self.last_verdict = res
        self.total_verifications = self.total_verifications + u256(1)
        
        return res

    @gl.public.view
    def get_last_result(self) -> str:
        return self.last_verdict

    @gl.public.view
    def get_stats(self) -> u256:
        return self.total_verifications
