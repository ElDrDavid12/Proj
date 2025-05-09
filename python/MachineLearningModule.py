import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.datasets import load_iris

# Define the environment (the agent will interact with)
class IrisEnv:
    def __init__(self, X, y):
        self.X = X
        self.y = y
        self.n_samples = len(X)
        self.current_sample = 0  # Start with the first sample
        self.action_space = 3  # Assume 3 classes (for Iris)
    
    def reset(self):
        self.current_sample = 0  # Reset to the first sample
        return self.X[self.current_sample]
    
    def step(self, action):
        # Action: classify into one of the three classes
        correct_class = self.y[self.current_sample]
        if action == correct_class:
            reward = 10  # Correct classification reward
        else:
            reward = -10  # Incorrect classification penalty
        self.current_sample += 1
        done = self.current_sample >= self.n_samples
        if done:
            self.current_sample = 0  # Reset if done (episode ends)
        return self.X[self.current_sample] if not done else None, reward, done

# Define the agent using Q-learning
class QLearningAgent:
    def __init__(self, state_space, action_space, alpha=0.1, gamma=0.9, epsilon=1.0):
        self.alpha = alpha  # Learning rate
        self.gamma = gamma  # Discount factor
        self.epsilon = epsilon  # Exploration rate
        self.state_space = state_space  # Number of samples (states)
        self.action_space = action_space  # Number of possible actions (classifications)
        self.q_table = np.zeros((state_space, action_space))  # Initialize Q-table with zeros
    
    def choose_action(self, state):
        # epsilon-greedy strategy for exploration and exploitation
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(range(self.action_space))  # Explore (random action)
        else:
            return np.argmax(self.q_table[state])  # Exploit (best action)

    def update_q_table(self, state, action, reward, next_state):
        # Q-learning update rule
        best_next_action = np.argmax(self.q_table[next_state]) if next_state is not None else 0
        old_q = self.q_table[state, action]
        new_q = old_q + self.alpha * (reward + self.gamma * self.q_table[next_state, best_next_action] - old_q)
        self.q_table[state, action] = new_q

    def decay_epsilon(self, episode, decay_rate=0.995):
        """Decay epsilon over time to encourage exploitation."""
        self.epsilon = max(0.1, self.epsilon * decay_rate)

# Load data (Iris dataset)
def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y

# Main function to run the reinforcement learning loop
def main():
    X, y = load_data()
    env = IrisEnv(X, y)
    agent = QLearningAgent(state_space=len(X), action_space=3)  # Three classes for Iris

    # Run the agent for a number of episodes
    episodes = 10_000  # Reduced number of episodes for faster results
    total_rewards = []

    for episode in range(episodes):
        state = env.reset()  # Reset the environment
        done = False
        total_reward = 0
        
        while not done:
            state_idx = env.current_sample  # Use current sample from environment as the state index
            action = agent.choose_action(state_idx)  # Choose an action (classification)
            next_state, reward, done = env.step(action)  # Take the action, get reward, and check if done
            agent.update_q_table(state_idx, action, reward, state_idx)  # Update Q-table
            total_reward += reward

        total_rewards.append(total_reward)

        # Decay epsilon over time for better exploration vs exploitation balance
        agent.decay_epsilon(episode)

        if (episode + 1) % 100 == 0:  # Print every 100 episodes
            print(f"Episode {episode + 1}: Total Reward: {total_reward}")

    # After learning, plot the total rewards over episodes
    plt.plot(total_rewards)
    plt.title("Total Rewards per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Total Reward")
    plt.show()

if __name__ == "__main__":
    main()
