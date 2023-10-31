import polib
from translate import Translator
from concurrent.futures import ThreadPoolExecutor
import math


if __name__ == "__main__":
    divider_num = 10
    source_pofile_path = "./paracraft_enUS.po"
    source_pofile = polib.pofile(source_pofile_path)
    fragment_num = math.floor(len(source_pofile) / divider_num)
    executor = ThreadPoolExecutor(max_workers=fragment_num)

    target_pofile = polib.POFile()

    def task(fragment_index):
        translator = Translator(from_lang="zh", to_lang="zh-tw")

        source_pofile_fragment = []
        if fragment_index < fragment_num - 1:
            source_pofile_fragment = source_pofile[fragment_index * divider_num - divider_num: fragment_index * divider_num]
        else:
            source_pofile_fragment = source_pofile[fragment_index * divider_num - divider_num: -fragment_index]

        target_fragment_pofile = polib.POFile()
        if len(source_pofile_fragment) > 0:
            for entry in source_pofile_fragment:
                print(entry)
                source_text = entry.msgid
                translated_text = ""
                try:
                    translated_text = translator.translate(source_text)
                except Exception as e:
                    print(e)
                entry.msgstr = translated_text
                target_fragment_pofile.append(entry)
        return {str(fragment_index): target_fragment_pofile}

    def handle_translated(fragments):
        for i in range(fragment_num):
            for j in fragments:
                temp = j.keys()
                temp_one = type(j.keys())
                if i == int(list(j.keys())[0]):
                    for entry in j["%d"%(i)]:
                        target_pofile.append(entry)

    futures = [executor.submit(task, i) for i in range(fragment_num)]
    target_pofile_fragments = []
    for future in futures:
        target_pofile_fragment = future.result()
        target_pofile_fragments.append(target_pofile_fragment)
    handle_translated(target_pofile_fragments)
    target_pofile.save("./paracraft_zh-tw.po")