#!/usr/bin/env python3
import sys
import re
import click
from transformers import AutoConfig, AutoTokenizer, AutoModelForSeq2SeqLM
class T5:
    def __init__(self, model_path):
        self._tokenizer = AutoTokenizer.from_pretrained(model_path)
        self._config = AutoConfig.from_pretrained(model_path)
        self._model = AutoModelForSeq2SeqLM.from_pretrained(model_path,config=self._config)

    def _generate(self, input_data, num):
        #インプットのトークン分け
        input_ids = self._tokenizer(input_data,
            max_length=50,
            truncation=True,
            return_tensors="pt").input_ids

        #生成
        output_ids = self._model.generate(input_ids,
            do_sample=True, #samplling
            top_k=50, #Top-K sampling
            num_return_sequences=num, #3つ候補を出す
            max_new_tokens=50, #最大長
            min_length=10, #最小長
            )

        #トークン分けた出力結果を生成文にデコード
        outputs = self._tokenizer.batch_decode(output_ids,
            skip_special_tokens=True #単に文字列
            )
        return outputs

    def do_interactive(self,input_data):
        while True:
            print('create a suggested message', file=sys.stderr)
            outputs = self._generate(input_data,3)
            print('choise a message>\n', file=sys.stderr)
            for i in range(len(outputs)):
                print(str(i)+ ') ' +outputs[i], file=sys.stderr)
            print('r) Reconsider messages', file=sys.stderr)
            print('a) Abort', file=sys.stderr)
            input_select=input()
            if(input_select == 'a'):
                break
            elif(input_select == 'r'):
                continue
            elif(re.match(f"[0-{len(outputs)}]", input_select)):
                print('Print a choise message to the stdout:', file=sys.stderr)
                print(outputs[int(input_select)], file=sys.stdout)
                return outputs[int(input_select)]
            else:
                print('unknown selecton;' +input_select, file=sys.stderr)
                break

    def do_quiet(self,input_data):
            print('suggested commit message', file=sys.stderr)
            output = self._generate(input_data,1)[0]
            print(f"{output}", file=sys.stdout)
            return output

@click.command()
@click.option('--model', help='a T5 Model path. default is a sample.', type=str, default='mamiksik/T5-commit-message-generation')
@click.option('--input_data', help='input text. default is a sample.', type=str, default="- tokenizer = AutoTokenizer.from_pretrained(\"example/ModelName\")\n+ tokenizer = AutoTokenizer.from_pretrained(\"mamiksik/T5-commit-message-generation\")")
@click.option('-q', help='non interactive mode', type=bool, is_flag=True)
def main(model, input_data, q):
    print('diff >\n' +input_data, file=sys.stderr)
    llm = T5(model)
    if(q):
        llm.do_quiet(input_data)
    else:
        llm.do_interactive(input_data)

if __name__ == "__main__":
    main()

