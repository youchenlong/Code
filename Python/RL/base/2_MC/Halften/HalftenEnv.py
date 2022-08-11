import gym
from gym import spaces
from gym.utils import seeding

# 一张牌
deck = [1,2,3,4,5,6,7,8,9,10,0.5,0.5,0.5]
# 人牌值
p_val = 0.5
# 限定值
dest = 10.5
# 随机发牌
def draw_card(np_random):
    return np_random.choice(deck)
# 随机发到手一张牌
def draw_hand(np_random):
    return [draw_card(np_random)]
# 当前手牌总分
def sum_hand(hand):
    return sum(hand)
# 获取手牌的数量
def get_card_num(hand):
    return len(hand)
# 获取手牌中的人牌数
def get_p_num(hand):
    count = 0
    for i in hand:
        if i == p_val:
            count += 1
    return count
# 爆牌
def get_bust(hand):
    return sum_hand(hand) > dest
# 十点半
def is_dest(hand):
    return sum_hand(hand) == dest
# 小于十点半
def lt_dest(hand):
    return sum_hand(hand) < dest
# 人五小
def is_rwx(hand):
    return True if get_p_num(hand) == 5 else False
# 天王
def is_tw(hand):
    return True if get_card_num(hand) == 5 and is_dest(hand) else False
# 五小
def is_wx(hand):
    return True if get_card_num(hand) == 5 and lt_dest(hand) else False
# 根据手牌返回结果
def hand_types(hand):
    type = 1
    reward = 1
    done = False
    if get_bust(hand):
        type = 0
        reward = -1
        done = True
    elif is_rwx(hand):
        type = 5
        reward = 5
        done = True
    elif is_tw(hand):
        type = 4
        reward = 4
        done = True
    elif is_wx(hand):
        type = 3
        reward = 3
        done = True
    elif is_dest(hand):
        type = 2
        reward = 2
        done = True
    return type, reward, done
# 庄家和玩家比较手牌
def cmp(dealer, player):
    dealer_score = sum_hand(dealer)
    player_score = sum_hand(player)
    if dealer_score > player_score:
        return True
    elif dealer_score < player_score:
        return False
    else:
        dealer_num = get_card_num(dealer)
        player_num = get_card_num(player)
        return True if dealer_num > player_num else False
        
class HalftenEnv(gym.Env):
    def __init__(self):
        self.action_space = spaces.Discrete(2) # 停牌，叫牌
        self.observation_space = spaces.Tuple((
            spaces.Discrete(21),    # 玩家当前手牌积分
            spaces.Discrete(5),     # 手牌数
            spaces.Discrete(6)))    # 人牌数
        self._seed()
        self._reset()
        self.nA = 2
    # 获取随机种子
    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    # 基于当前的状态和动作，得出下一步的状态、回报、是否结束
    def _step(self, action):
        assert self.action_space.contains(action)
        reward = 0
        if action:
            self.player.append(draw_card(self.np_random))
            type, reward, done = hand_types(self.player)
        else:
            done = True
            self.dealer = draw_hand(self.np_random)
            result = cmp(self.dealer, self.player)
            if result:
                reward = -1
            else:
                while not result:
                    self.dealer.append(draw_card(self.np_random))
                    dealer_type, dealer_reward, dealer_done = hand_types(self.dealer)
                    if dealer_done:
                        reward = -dealer_reward
                        break
                    result = cmp(self.dealer, self.player)
                    if result:
                        reward = -1
                        break
        return self._get_obs(), reward, done, {}
    # 获取当前的状态空间
    def _get_obs(self):
        return (sum_hand(self.player), get_card_num(self.player), get_p_num(self.player))
    # 牌局初始化
    def _reset(self):
        self.player = draw_hand(self.np_random)
        return self._get_obs()