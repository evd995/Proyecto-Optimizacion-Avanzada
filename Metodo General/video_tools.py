import cv2
import numpy as np

def load_video(path):
    video = cv2.VideoCapture(path)
    
    size = None
    M = None # Video como matriz

    try: 
        while video.isOpened():
            ret, frame = video.read()
            
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                size = frame.shape
                
                if M is None:
                    M = frame.flatten()
                else:
                    M = np.column_stack((M, frame.flatten()))
            else:
                break
    finally:
        video.release()
    
    return M, size

def save_demo_video(path, D, L, S):
    """
    Funcion pensada para guardar especificamente el video del
    demo.
    
    Primera fila, D
    Segunda fila, S
    Tercera fila, L
    """
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path, fourcc, 20.0, (100,300))


    try:
        print('Creating Video')
        for i in range(L.shape[1]):
            D_frame = D[:, i].reshape(100,100).astype(np.uint8)
            D_frame = cv2.cvtColor(D_frame, cv2.COLOR_GRAY2BGR)
            
            L_frame = L[:, i].reshape(100,100).astype(np.uint8)
            L_frame = cv2.cvtColor(L_frame, cv2.COLOR_GRAY2BGR)

            S_frame = S[:, i].reshape(100,100).astype(np.uint8)
            S_frame = cv2.cvtColor(S_frame, cv2.COLOR_GRAY2BGR)

            out.write(cv2.vconcat([D_frame, L_frame, S_frame]))
    finally:
        print('Releasing Video')
        out.release()
        
def save_video(path, video_size, D, L, S):
    """
    Funcion pensada para guardar especificamente el video del
    demo.
    
    Primera fila, D
    Segunda fila, S
    Tercera fila, L
    """
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path, fourcc, 20.0, (video_size[1],3*video_size[0]))


    try:
        print('Creating Video')
        for i in range(L.shape[1]):
            D_frame = D[:, i].reshape(video_size).astype(np.uint8)
            D_frame = cv2.cvtColor(D_frame, cv2.COLOR_GRAY2BGR)
            
            L_frame = L[:, i].reshape(video_size).astype(np.uint8)
            L_frame = cv2.cvtColor(L_frame, cv2.COLOR_GRAY2BGR)

            S_frame = S[:, i].reshape(video_size).astype(np.uint8)
            S_frame = cv2.cvtColor(S_frame, cv2.COLOR_GRAY2BGR)

            out.write(cv2.vconcat([D_frame, L_frame, S_frame]))
    finally:
        print('Releasing Video')
        out.release()