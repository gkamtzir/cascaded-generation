CUDA_VISIBLE_DEVICES=3 fairseq-generate ../fairseq_vanilla/data-bin/wmt16_ro_en_joint  --path /n/rush_lab/users/y/checkpoints/barrier/ro-en-mlm-3gpu-largelr-fix/checkpoint105.pt --batch-size 1 --topk 32 --rounds 5 --remove-bpe --D 3 --max-len-a 0.9247462305812968 --max-len-b 1.1175631354616158 --gen-subset valid --max-size 3000 --seed 1234 > /n/rush_lab/users/y/val_ab_logs/wmt-ro-en-epoch-ab-fixD0/topk32_D3_rounds5_speed.txt 2>&1
CUDA_VISIBLE_DEVICES=3 fairseq-generate ../fairseq_vanilla/data-bin/wmt16_ro_en_joint  --path /n/rush_lab/users/y/checkpoints/barrier/ro-en-mlm-3gpu-largelr-fix/checkpoint105.pt --batch-size 1 --topk 128 --rounds 5 --remove-bpe --D 3 --max-len-a 0.9247462305812968 --max-len-b 1.1175631354616158 --gen-subset valid --max-size 3000 --seed 1234 > /n/rush_lab/users/y/val_ab_logs/wmt-ro-en-epoch-ab-fixD0/topk128_D3_rounds5_speed.txt 2>&1