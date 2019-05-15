import argparse


def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu')
    parser.add_argument('--path_data')
    parser.add_argument('--folder')
    parser.add_argument('--train', type=int)
    parser.add_argument('--image_channels', type=int)
    parser.add_argument('--file_model', default='model.pth')
    parser.add_argument('--file_result_base', default='result_{}.h5')
    parser.add_argument('--predict_back', type=int, default=1)
    parser.add_argument('--batch_size', type=int, default=128)
    parser.add_argument('--num_workers', type=int, default=1)
    parser.add_argument('--num_tests', type=int, default=5)
    parser.add_argument('--num_steps', type=int, default=2)
    parser.add_argument('--num_epochs', type=int, default=100)
    parser.add_argument('--epoch_split_recon', type=int, default=50)
    parser.add_argument('--epoch_split_back', type=int, default=50)
    parser.add_argument('--max_objects', type=int, default=4)
    parser.add_argument('--image_full_size', type=int, default=48)
    parser.add_argument('--image_crop_size', type=int, default=20)
    parser.add_argument('--gaussian_std', type=float, default=0.3)
    parser.add_argument('--lr', type=float, default=1e-4)
    parser.add_argument('--loss_weights', type=float, nargs='+', default=None)
    # InitializerWhere and UpdaterWhere
    parser.add_argument('--state_size_base', type=int, default=256)
    parser.add_argument('--state_size_where', type=int, default=256)
    parser.add_argument('--init_where_channels', type=int, nargs='+', default=[8, 8, 16, 16])
    parser.add_argument('--init_where_resample', type=int, nargs='+', default=[0, 1, 0, 1])
    parser.add_argument('--init_where_hidden_1', type=int, nargs='+', default=[256])
    parser.add_argument('--init_where_hidden_2', type=int, nargs='+', default=[256, 256])
    parser.add_argument('--upd_where_channels', type=int, nargs='+', default=[8, 8, 16, 16])
    parser.add_argument('--upd_where_resample', type=int, nargs='+', default=[0, 1, 0, 1])
    parser.add_argument('--upd_where_hidden', type=int, nargs='+', default=[256])
    # InitializerWhat and UpdaterWhat
    parser.add_argument('--state_size_what', type=int, default=256)
    parser.add_argument('--init_what_channels', type=int, nargs='+', default=[8, 8, 16, 16])
    parser.add_argument('--init_what_resample', type=int, nargs='+', default=[0, 1, 0, 1])
    parser.add_argument('--init_what_hidden', type=int, nargs='+', default=[256])
    parser.add_argument('--upd_what_channels', type=int, nargs='+', default=[8, 8, 16, 16])
    parser.add_argument('--upd_what_resample', type=int, nargs='+', default=[0, 1, 0, 1])
    parser.add_argument('--upd_what_hidden', type=int, nargs='+', default=[256])
    # InitializerBack and UpdaterBack
    parser.add_argument('--state_size_back', type=int, default=256)
    parser.add_argument('--init_back_channels', type=int, nargs='+', default=[8, 8, 16, 16])
    parser.add_argument('--init_back_resample', type=int, nargs='+', default=[0, 1, 0, 1])
    parser.add_argument('--init_back_hidden', type=int, nargs='+', default=[256])
    parser.add_argument('--upd_back_channels', type=int, nargs='+', default=[8, 8, 16, 16])
    parser.add_argument('--upd_back_resample', type=int, nargs='+', default=[0, 1, 0, 1])
    parser.add_argument('--upd_back_hidden', type=int, nargs='+', default=[256])
    # VAEPres
    parser.add_argument('--vae_pres_alpha', type=float, default=1e-3)
    parser.add_argument('--enc_pres_hidden', type=int, nargs='+', default=[128, 64])
    # VAEScaleTrans
    parser.add_argument('--vae_scl_trs_mu', type=float, nargs='+', default=[0., 0., 0., 0.])
    parser.add_argument('--vae_scl_trs_std', type=float, nargs='+', default=[0.5, 0.5, 0.5, 0.5])
    parser.add_argument('--enc_scl_trs_hidden', type=int, nargs='+', default=[256, 256])
    # VAEShapeAppear
    parser.add_argument('--vae_size_shp', type=int, default=32)
    parser.add_argument('--vae_size_apc', type=int, default=32)
    parser.add_argument('--enc_shp_apc_hidden', type=int, nargs='+', default=[256])
    parser.add_argument('--dec_shp_hidden', type=int, nargs='+', default=[256])
    parser.add_argument('--dec_shp_channels', type=int, nargs='+', default=[8, 8, 16, 16])
    parser.add_argument('--dec_shp_resample', type=int, nargs='+', default=[0, 1, 0, 1])
    parser.add_argument('--dec_apc_hidden', type=int, nargs='+', default=[16, 16])
    # VAEBack
    parser.add_argument('--vae_size_back', type=int, default=32)
    parser.add_argument('--enc_back_hidden', type=int, nargs='+', default=[256])
    parser.add_argument('--dec_back_hidden', type=int, nargs='+', default=[16, 16])
    parser.add_argument('--coef_back', type=float, default=1.)
    args = parser.parse_args()
    args.loss_weights = args.loss_weights if args.loss_weights is not None else [1.] * (args.num_steps + 1)
    return args