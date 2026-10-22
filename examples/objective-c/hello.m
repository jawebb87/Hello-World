#import <Foundation/Foundation.h>
#include <stdio.h>

int main(void) {
    @autoreleasepool {
        NSString *greeting = @"Hello, world!";
        puts([greeting UTF8String]);
    }
    return 0;
}
