import os
import pandas as pd
import pprint as pp
import numpy as np

FMRI_GRASPS = ['point', 'power', 'pinch', 'wrist_ext', 'wrist_flex']
GRASPS = ['point', 'power', 'pinch', 'wrist_ext', 'wrist_flex',
            'tripod', 'key', 'iflex', 'wrot', 'rpower']
LIMBS = ['R', 'L']


def longest_trail(limb_order):
    """This function computes the length of the longest contiguous subsequence in limb_order where the same limb
    (e.g., 'R' or 'L') appears consecutively. It iterates through the list, comparing each element to the start of a
     current chain and updates the longest chain length when a match continues."""
    current_chain = 0
    longest_chain = 0
    p = 0
    q = 0
    for i in range(1, len(limb_order)):
        if limb_order[p] == limb_order[i]:
            q = i
            current_chain = q - p + 1
            if longest_chain < current_chain:
                longest_chain = current_chain
        else:
            p = i
            current_chain = 0
    print('longest chain', longest_chain)
    return longest_chain


def random_limb_order(limb_names, num_grasps):
    """This function generates a randomized sequence of limbs such that no more than two of the same limb appear
    consecutively. It constructs an initial list by repeating the limb names, shuffles it, and reshuffles until the
     longest_trail is 2 or less."""
    limb_sequence = limb_names * num_grasps
    np.random.shuffle(limb_sequence)

    longest_consecutive = longest_trail(limb_sequence)
    while longest_consecutive > 2:
        np.random.shuffle(limb_sequence)
        longest_consecutive = longest_trail(limb_sequence)

    return limb_sequence


def generate_trial_conditions(limb_names, num_runs, grasps):
    """This function creates randomized trial conditions for a given number of runs, combining grasp types and limb
    sequences. For each run, it generates a limb sequence using random_limb_order, creates a shuffled list of grasps
    (duplicated to match limb count), and merges them into run-wise condition strings (e.g., "R_power")."""
    grasps_by_run = []
    for k in range(num_runs):
        limb_sequence = random_limb_order(limb_names, len(grasps))
        # for good measure shuffle the order of grasps
        for _ in range(4):
            np.random.shuffle(grasps)
        r_grasps = grasps.copy()
        np.random.shuffle(grasps)
        l_grasps = grasps.copy()
        run_sequence = []
        for limb in limb_sequence:
            if limb == 'L':
                run_sequence += ['L' + '-' + l_grasps.pop(0)]
            else:
                run_sequence += ['R' + '-' + r_grasps.pop(0)]
        grasps_by_run += [run_sequence]
    return grasps_by_run


def save_trials_to_excel(grasps_by_run, output_dir='runs_output'):
    os.makedirs(output_dir, exist_ok=True)

    for i, run in enumerate(grasps_by_run):
        rows1 = []
        rows2 = []
        for k in range(0, len(run)):
            item = run[k]
            side, grasp = item.split('-')
            if k < 10:
                rows1.append({
                    'image': f'stimuli/{grasp}_{side}.png',
                    'grasp': grasp,
                    'side': side
                })
            else:
                rows2.append({
                    'image': f'stimuli/{grasp}_{side}.png',
                    'grasp': grasp,
                    'side': side
                })
        df = pd.DataFrame(rows1)
        file_path = os.path.join(output_dir, f'run_{i + 1}A.csv')
        df.to_csv(file_path, index=False)
        
        df = pd.DataFrame(rows2)
        file_path = os.path.join(output_dir, f'run_{i + 1}B.csv')
        df.to_csv(file_path, index=False)

    print(f"Saved {len(grasps_by_run)} Excel files to '{output_dir}/'.")


if __name__ == '__main__':
    grasps_by_run = generate_trial_conditions(LIMBS, 5, GRASPS)
    pp.pprint(grasps_by_run)
    save_trials_to_excel(grasps_by_run, output_dir='runs_output')
