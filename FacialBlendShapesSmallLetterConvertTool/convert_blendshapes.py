import bpy
import sys
import os

def convert_uppercase_blendshapes():
    # Body 오브젝트 찾기
    body_obj = None
    for obj in bpy.data.objects:
        if obj.name == "Body":
            body_obj = obj
            break
    
    if body_obj is None:
        print("'Body' 오브젝트를 찾을 수 없습니다.")
        return
    
    # 블렌드셰입이 있는지 확인
    if not body_obj.data.shape_keys:
        print("Body 오브젝트에 블렌드셰입이 없습니다.")
        return
    
    # 변환된 블렌드셰입 수 카운트
    converted_count = 0
    
    # 모든 블렌드셰입 검사
    for key in body_obj.data.shape_keys.key_blocks:
        # 첫 글자가 대문자인지 확인
        if key.name and key.name[0].isupper():
            # 새 이름 생성 (첫 글자를 소문자로)
            new_name = key.name[0].lower() + key.name[1:]
            print(f"변환: {key.name} -> {new_name}")
            # 이름 변경
            key.name = new_name
            converted_count += 1
    
    if converted_count > 0:
        print(f"\n총 {converted_count}개의 블렌드셰입이 변환되었습니다.")
    else:
        print("\n변환할 대문자 블렌드셰입이 없습니다.")

def main():
    # FBX 파일 경로 확인
    if len(sys.argv) < 2:
        print("사용법: blender --background --python convert_blendshapes.py -- [FBX파일경로]")
        return
    
    # FBX 파일 경로 가져오기
    fbx_file = sys.argv[-1]
    
    if not os.path.exists(fbx_file):
        print(f"파일을 찾을 수 없습니다: {fbx_file}")
        return
    
    # 기존 데이터 초기화
    bpy.ops.wm.read_factory_settings(use_empty=True)
    
    # FBX 파일 임포트
    bpy.ops.import_scene.fbx(filepath=fbx_file)
    
    # 변환 실행
    convert_uppercase_blendshapes()
    
    # 결과 저장 (원본 파일과 동일한 이름으로 저장)
    output_file = fbx_file
    bpy.ops.export_scene.fbx(
        filepath=output_file,
        use_selection=False,
        apply_scale_options='FBX_SCALE_ALL',
        bake_space_transform=True,
        add_leaf_bones=False,
        use_metadata=True,
        path_mode='AUTO'
    )
    
    print(f"\n변환된 파일이 저장되었습니다: {output_file}")

if __name__ == "__main__":
    main() 