#include<stdio.h>
#include<math.h>

void plus(char* c, char* a, char* b){
    c[1] = a[1] * b[1];
    a[0] *= b[1];
    b[0] *= a[1];
    c[0] = a[0] + b[0];
    return;
}
void multi(char c[2], char a[2], char b[2]){
    c[1] = a[1] * b[1];
    c[0] = a[0] * b[0];
    return;
}
void simp(char c[2]){
    int max = (c[0] > c[1]) ? c[0] : c[1];
    for(int i = 2;i <= sqrt(max); ++i){
        while ((c[0]%i == 0)&&(c[1]%i == 0)){
            c[0] /= i;
            c[1] /= i;
        }
    }
    return;
}

int main(){
    char nums[2][4] = {{0},{0}};
    char op[2] = {0};
    char digits[3][2] = {0};
    char ans[6] = {0};
    char buf[6] = {0};
    int pointer = 0;
    int tp = 0;
    int flag = 0;
    printf("Please input your expression: ");
    scanf("%s %s %s",nums[0], op, nums[1]);
    for(int i = 0;i < 2;++i){
        while((nums[i][pointer] != '/')&&(nums[i][pointer])){
            buf[pointer] = nums[i][pointer];
            ++pointer;
        }
        if (buf[1])
            digits[i][0] = (buf[0] - 48) * 10 + buf[1] - 48;
        else if(buf[0])
            digits[i][0] = buf[0] - 48;
        else
            digits[i][0] = 1;
        tp = pointer + 1;
        pointer = 0;
        buf[0] = 0;
        buf[1] = 0;
        buf[2] = 0;
        while((nums[i][tp + pointer])){
            buf[pointer] = nums[i][tp + pointer];
            ++pointer;
        }
        if (buf[1])
            digits[i][1] = (buf[0] - 48) * 10 + buf[1] - 48;
        else if(buf[0])
            digits[i][1] = buf[0] - 48;
        else
            digits[i][1] = 1;
        pointer = 0;
    }
    if (op[0] == '+'){
        plus(digits[2], digits[0], digits[1]);
        simp(digits[2]);
    }
    else if (op[0] == '-'){
        digits[1][0] *= -1;
        plus(digits[2], digits[0], digits[1]);
        simp(digits[2]);
    }
    else if (op[0] == '*'){
        multi(digits[2], digits[0], digits[1]);
        simp(digits[2]);
    }
    else if (op[0] == '/'){
        char tmp = digits[1][0];
        digits[1][0] = digits[1][1];
        digits[1][1] = tmp;
        multi(digits[2], digits[0], digits[1]);
        simp(digits[2]);
    }
    if (digits[2][0] < 0){
        digits[2][0] *= -1;
        flag = 1;
    }

    if (digits[2][1] != 1){
        if (digits[2][0] > 9){
            ans[pointer++] = digits[2][0]/10 + 48;
            ans[pointer++] = digits[2][0]%10 + 48;
        }
        else{
            ans[pointer++] = digits[2][0] + 48;
        }
        ans[pointer++] = '/';
        if (digits[2][1] > 9){
            ans[pointer++] = digits[2][1]/10 + 48;
            ans[pointer++] = digits[2][1]%10 + 48;
        }
        else{
            ans[pointer++] = digits[2][1] + 48;
        }
    }
    else{
        ans[0] = digits[2][0] + 48;
    }
    if (flag == 0)
        printf("%s %s %s = %s", nums[0], op, nums[1], ans);
    else{
        printf("%s %s %s = -%s", nums[0], op, nums[1], ans);
    }
    return 0;
}