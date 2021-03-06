from darkflow.utils.attr_utils import AttributeDict
import json
import argparse


def parse():
    parser = argparse.ArgumentParser(description="darkflow_configs")
    parser.add_argument('--mode', type=str, default='training', choices=['training', 'testing'], help='Choose if are you training or testing the model')
    parser.add_argument('--configs_file', type=str, default='/home/pjawahar/Projects/DarkFlow/darkflow/configs/configs.json')
    parser.add_argument('--network', type=str, default='convnet', choices=['convnet'])
    parser.add_argument('--flow', type=str, default='noflow', choices=['noflow', 'planar', 'orthosnf', 'householdersnf', 'triangularsnf', 'iaf', 'convflow'])
    args = parser.parse_args()
    return args


def run(args):
    if args.mode == 'training':
        print('Preparing to Train Model')
        args.train_net = 1
    elif args.mode == 'testing':
        print('Preparing to Test Model')
        args.test_net = 1
    else:
        raise argparse.ArgumentTypeError('Run mode not chosen correctly. Choose if you want to train (--mode training) or test (--mode testing).')

    if args.network == 'convnet':
        from darkflow.runners.convnet_runner import ConvNetRunner
        network = ConvNetRunner(args=args)

        if args.train_net:
            network.trainer()
            
        if args.test_net:
            network.tester()
    

if __name__ == '__main__':
    args = parse().__dict__
    configs = json.load(open(args['configs_file']))
    configs = {**configs, **args}
    configs = AttributeDict(configs)
    run(configs)