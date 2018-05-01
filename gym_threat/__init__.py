from gym.envs.registration import register

register(
    id='threat-v0',
    entry_point='gym_threat.envs:ThreatEnv',
)