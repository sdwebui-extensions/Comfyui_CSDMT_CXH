from .lib.ximg import *

class CSD:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "sources": ("IMAGE",),
                "makeup": ("IMAGE",),
                "reszie": ([256, 512],),
                "inittype": (["normal", "xavier"," kaiming","orthogonal"],),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("out",)
    FUNCTION = "gen"
    OUTPUT_NODE = False
    CATEGORY = "CXH"

    def gen(self, sources,makeup,reszie,inittype):
        from .CSD_MT_eval import makeup_transfer256

        mask_results = []
        makeup_img = np.clip(255.0 * makeup.cpu().numpy().squeeze(), 0, 255).astype(np.uint8) #tensor2pil(makeup)

        for img in sources:
            non_makeup_img = np.clip(255.0 * img.cpu().numpy().squeeze(), 0, 255).astype(np.uint8) #tensor2pil(img)
            resp = makeup_transfer256(non_makeup_img,makeup_img,reszie,inittype)
                
            mask_results.append(pil2tensor(resp))   

        # 将结果列表中的张量连接在一起
        return (torch.cat(mask_results, dim=0),)


