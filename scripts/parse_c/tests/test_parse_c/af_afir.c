# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c"
# 1 "<built-in>" 1
# 1 "<built-in>" 3
# 418 "<built-in>" 3
# 1 "<command line>" 1
# 1 "<built-in>" 2
# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2
# 26 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/float.h" 1 3
# 32 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/float.h" 3
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/float.h" 1 3 4
# 33 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/float.h" 2 3
# 27 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2

# 1 "./libavutil/cpu.h" 1
# 24 "./libavutil/cpu.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 35 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 3
typedef long int ptrdiff_t;
# 46 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 3
typedef long unsigned int size_t;
# 74 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 3
typedef int wchar_t;
# 103 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 3
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/__stddef_max_align_t.h" 1 3
# 16 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/__stddef_max_align_t.h" 3
typedef long double max_align_t;
# 104 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 2 3
# 25 "./libavutil/cpu.h" 2
# 100 "./libavutil/cpu.h"
int av_get_cpu_flags(void);





void av_force_cpu_flags(int flags);






int av_parse_cpu_caps(unsigned *flags, const char *s);




int av_cpu_count(void);





void av_cpu_force_count(int count);
# 135 "./libavutil/cpu.h"
size_t av_cpu_max_align(void);
# 29 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2
# 1 "./libavutil/tx.h" 1
# 22 "./libavutil/tx.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stdint.h" 1 3
# 52 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stdint.h" 3
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 1 3 4
# 18 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_int8_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_int8_t.h" 3 4
typedef signed char int8_t;
# 19 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_int16_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_int16_t.h" 3 4
typedef short int16_t;
# 20 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_int32_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_int32_t.h" 3 4
typedef int int32_t;
# 21 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_int64_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_int64_t.h" 3 4
typedef long long int64_t;
# 22 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint8_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint8_t.h" 3 4
typedef unsigned char uint8_t;
# 24 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint16_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint16_t.h" 3 4
typedef unsigned short uint16_t;
# 25 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint32_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint32_t.h" 3 4
typedef unsigned int uint32_t;
# 26 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint64_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uint64_t.h" 3 4
typedef unsigned long long uint64_t;
# 27 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4


typedef int8_t int_least8_t;
typedef int16_t int_least16_t;
typedef int32_t int_least32_t;
typedef int64_t int_least64_t;
typedef uint8_t uint_least8_t;
typedef uint16_t uint_least16_t;
typedef uint32_t uint_least32_t;
typedef uint64_t uint_least64_t;



typedef int8_t int_fast8_t;
typedef int16_t int_fast16_t;
typedef int32_t int_fast32_t;
typedef int64_t int_fast64_t;
typedef uint8_t uint_fast8_t;
typedef uint16_t uint_fast16_t;
typedef uint32_t uint_fast32_t;
typedef uint64_t uint_fast64_t;




# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types.h" 1 3 4
# 32 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h" 1 3 4
# 678 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_symbol_aliasing.h" 1 3 4
# 679 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h" 2 3 4
# 744 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_posix_availability.h" 1 3 4
# 745 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/cdefs.h" 2 3 4
# 33 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/_types.h" 1 3 4
# 34 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/_types.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_types.h" 1 3 4
# 15 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_types.h" 3 4
typedef signed char __int8_t;



typedef unsigned char __uint8_t;
typedef short __int16_t;
typedef unsigned short __uint16_t;
typedef int __int32_t;
typedef unsigned int __uint32_t;
typedef long long __int64_t;
typedef unsigned long long __uint64_t;

typedef long __darwin_intptr_t;
typedef unsigned int __darwin_natural_t;
# 48 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_types.h" 3 4
typedef int __darwin_ct_rune_t;





typedef union {
 char __mbstate8[128];
 long long _mbstateL;
} __mbstate_t;

typedef __mbstate_t __darwin_mbstate_t;


typedef long int __darwin_ptrdiff_t;







typedef long unsigned int __darwin_size_t;





typedef __builtin_va_list __darwin_va_list;





typedef int __darwin_wchar_t;




typedef __darwin_wchar_t __darwin_rune_t;


typedef int __darwin_wint_t;




typedef unsigned long __darwin_clock_t;
typedef __uint32_t __darwin_socklen_t;
typedef long __darwin_ssize_t;
typedef long __darwin_time_t;
# 35 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/_types.h" 2 3 4
# 34 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types.h" 2 3 4
# 55 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types.h" 3 4
typedef __int64_t __darwin_blkcnt_t;
typedef __int32_t __darwin_blksize_t;
typedef __int32_t __darwin_dev_t;
typedef unsigned int __darwin_fsblkcnt_t;
typedef unsigned int __darwin_fsfilcnt_t;
typedef __uint32_t __darwin_gid_t;
typedef __uint32_t __darwin_id_t;
typedef __uint64_t __darwin_ino64_t;

typedef __darwin_ino64_t __darwin_ino_t;



typedef __darwin_natural_t __darwin_mach_port_name_t;
typedef __darwin_mach_port_name_t __darwin_mach_port_t;
typedef __uint16_t __darwin_mode_t;
typedef __int64_t __darwin_off_t;
typedef __int32_t __darwin_pid_t;
typedef __uint32_t __darwin_sigset_t;
typedef __int32_t __darwin_suseconds_t;
typedef __uint32_t __darwin_uid_t;
typedef __uint32_t __darwin_useconds_t;
typedef unsigned char __darwin_uuid_t[16];
typedef char __darwin_uuid_string_t[37];

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h" 1 3 4
# 57 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_types.h" 3 4
struct __darwin_pthread_handler_rec {
 void (*__routine)(void *);
 void *__arg;
 struct __darwin_pthread_handler_rec *__next;
};

struct _opaque_pthread_attr_t {
 long __sig;
 char __opaque[56];
};

struct _opaque_pthread_cond_t {
 long __sig;
 char __opaque[40];
};

struct _opaque_pthread_condattr_t {
 long __sig;
 char __opaque[8];
};

struct _opaque_pthread_mutex_t {
 long __sig;
 char __opaque[56];
};

struct _opaque_pthread_mutexattr_t {
 long __sig;
 char __opaque[8];
};

struct _opaque_pthread_once_t {
 long __sig;
 char __opaque[8];
};

struct _opaque_pthread_rwlock_t {
 long __sig;
 char __opaque[192];
};

struct _opaque_pthread_rwlockattr_t {
 long __sig;
 char __opaque[16];
};

struct _opaque_pthread_t {
 long __sig;
 struct __darwin_pthread_handler_rec *__cleanup_stack;
 char __opaque[8176];
};

typedef struct _opaque_pthread_attr_t __darwin_pthread_attr_t;
typedef struct _opaque_pthread_cond_t __darwin_pthread_cond_t;
typedef struct _opaque_pthread_condattr_t __darwin_pthread_condattr_t;
typedef unsigned long __darwin_pthread_key_t;
typedef struct _opaque_pthread_mutex_t __darwin_pthread_mutex_t;
typedef struct _opaque_pthread_mutexattr_t __darwin_pthread_mutexattr_t;
typedef struct _opaque_pthread_once_t __darwin_pthread_once_t;
typedef struct _opaque_pthread_rwlock_t __darwin_pthread_rwlock_t;
typedef struct _opaque_pthread_rwlockattr_t __darwin_pthread_rwlockattr_t;
typedef struct _opaque_pthread_t *__darwin_pthread_t;
# 81 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types.h" 2 3 4
# 53 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_intptr_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_intptr_t.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/types.h" 1 3 4
# 37 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/types.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/types.h" 1 3 4
# 60 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/types.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int8_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int8_t.h" 3 4
typedef unsigned char u_int8_t;
# 61 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/types.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int16_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int16_t.h" 3 4
typedef unsigned short u_int16_t;
# 62 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/types.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int32_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int32_t.h" 3 4
typedef unsigned int u_int32_t;
# 63 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/types.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int64_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_u_int64_t.h" 3 4
typedef unsigned long long u_int64_t;
# 64 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/types.h" 2 3 4


typedef int64_t register_t;




# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_intptr_t.h" 1 3 4
# 72 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/types.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_uintptr_t.h" 1 3 4
# 34 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_uintptr_t.h" 3 4
typedef unsigned long uintptr_t;
# 73 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/types.h" 2 3 4




typedef u_int64_t user_addr_t;
typedef u_int64_t user_size_t;
typedef int64_t user_ssize_t;
typedef int64_t user_long_t;
typedef u_int64_t user_ulong_t;
typedef int64_t user_time_t;
typedef int64_t user_off_t;
# 104 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/types.h" 3 4
typedef u_int64_t syscall_arg_t;
# 38 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/types.h" 2 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_intptr_t.h" 2 3 4

typedef __darwin_intptr_t intptr_t;
# 54 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4




# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_intmax_t.h" 1 3 4
# 32 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_intmax_t.h" 3 4
typedef long int intmax_t;
# 59 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uintmax_t.h" 1 3 4
# 32 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types/_uintmax_t.h" 3 4
typedef long unsigned int uintmax_t;
# 60 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdint.h" 2 3 4
# 53 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stdint.h" 2 3
# 23 "./libavutil/tx.h" 2
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 24 "./libavutil/tx.h" 2

typedef struct AVTXContext AVTXContext;

typedef struct AVComplexFloat {
    float re, im;
} AVComplexFloat;

typedef struct AVComplexDouble {
    double re, im;
} AVComplexDouble;

typedef struct AVComplexInt32 {
    int32_t re, im;
} AVComplexInt32;

enum AVTXType {







    AV_TX_FLOAT_FFT = 0,
    AV_TX_DOUBLE_FFT = 2,
    AV_TX_INT32_FFT = 4,
# 68 "./libavutil/tx.h"
    AV_TX_FLOAT_MDCT = 1,
    AV_TX_DOUBLE_MDCT = 3,
    AV_TX_INT32_MDCT = 5,
# 90 "./libavutil/tx.h"
    AV_TX_FLOAT_RDFT = 6,
    AV_TX_DOUBLE_RDFT = 7,
    AV_TX_INT32_RDFT = 8,
# 104 "./libavutil/tx.h"
    AV_TX_FLOAT_DCT = 9,
    AV_TX_DOUBLE_DCT = 10,
    AV_TX_INT32_DCT = 11,
# 116 "./libavutil/tx.h"
    AV_TX_FLOAT_DCT_I = 12,
    AV_TX_DOUBLE_DCT_I = 13,
    AV_TX_INT32_DCT_I = 14,
# 128 "./libavutil/tx.h"
    AV_TX_FLOAT_DST_I = 15,
    AV_TX_DOUBLE_DST_I = 16,
    AV_TX_INT32_DST_I = 17,


    AV_TX_NB,
};
# 151 "./libavutil/tx.h"
typedef void (*av_tx_fn)(AVTXContext *s, void *out, void *in, ptrdiff_t stride);




enum AVTXFlags {




    AV_TX_INPLACE = 1ULL << 0,





    AV_TX_UNALIGNED = 1ULL << 1,







    AV_TX_FULL_IMDCT = 1ULL << 2,
# 184 "./libavutil/tx.h"
    AV_TX_REAL_TO_REAL = 1ULL << 3,
    AV_TX_REAL_TO_IMAGINARY = 1ULL << 4,
};
# 202 "./libavutil/tx.h"
int av_tx_init(AVTXContext **ctx, av_tx_fn *tx, enum AVTXType type,
               int inv, int len, const void *scale, uint64_t flags);




void av_tx_uninit(AVTXContext **ctx);
# 30 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2
# 1 "./libavutil/avstring.h" 1
# 24 "./libavutil/avstring.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 25 "./libavutil/avstring.h" 2

# 1 "./libavutil/attributes.h" 1
# 27 "./libavutil/avstring.h" 2
# 42 "./libavutil/avstring.h"
int av_strstart(const char *str, const char *pfx, const char **ptr);
# 54 "./libavutil/avstring.h"
int av_stristart(const char *str, const char *pfx, const char **ptr);
# 68 "./libavutil/avstring.h"
char *av_stristr(const char *haystack, const char *needle);
# 83 "./libavutil/avstring.h"
char *av_strnstr(const char *haystack, const char *needle, size_t hay_length);
# 100 "./libavutil/avstring.h"
size_t av_strlcpy(char *dst, const char *src, size_t size);
# 118 "./libavutil/avstring.h"
size_t av_strlcat(char *dst, const char *src, size_t size);
# 132 "./libavutil/avstring.h"
size_t av_strlcatf(char *dst, size_t size, const char *fmt, ...) __attribute__((__format__(__printf__, 3, 4)));
# 141 "./libavutil/avstring.h"
static inline size_t av_strnlen(const char *s, size_t len)
{
    size_t i;
    for (i = 0; i < len && s[i]; i++)
        ;
    return i;
}
# 157 "./libavutil/avstring.h"
char *av_asprintf(const char *fmt, ...) __attribute__((__format__(__printf__, 1, 2)));
# 173 "./libavutil/avstring.h"
char *av_get_token(const char **buf, const char *term);
# 197 "./libavutil/avstring.h"
char *av_strtok(char *s, const char *delim, char **saveptr);




static inline __attribute__((const)) int av_isdigit(int c)
{
    return c >= '0' && c <= '9';
}




static inline __attribute__((const)) int av_isgraph(int c)
{
    return c > 32 && c < 127;
}




static inline __attribute__((const)) int av_isspace(int c)
{
    return c == ' ' || c == '\f' || c == '\n' || c == '\r' || c == '\t' ||
           c == '\v';
}




static inline __attribute__((const)) int av_toupper(int c)
{
    if (c >= 'a' && c <= 'z')
        c ^= 0x20;
    return c;
}




static inline __attribute__((const)) int av_tolower(int c)
{
    if (c >= 'A' && c <= 'Z')
        c ^= 0x20;
    return c;
}




static inline __attribute__((const)) int av_isxdigit(int c)
{
    c = av_tolower(c);
    return av_isdigit(c) || (c >= 'a' && c <= 'f');
}





int av_strcasecmp(const char *a, const char *b);





int av_strncasecmp(const char *a, const char *b, size_t n);





char *av_strireplace(const char *str, const char *from, const char *to);
# 279 "./libavutil/avstring.h"
const char *av_basename(const char *path);
# 289 "./libavutil/avstring.h"
const char *av_dirname(char *path);
# 302 "./libavutil/avstring.h"
int av_match_name(const char *name, const char *names);
# 312 "./libavutil/avstring.h"
char *av_append_path_component(const char *path, const char *component);

enum AVEscapeMode {
    AV_ESCAPE_MODE_AUTO,
    AV_ESCAPE_MODE_BACKSLASH,
    AV_ESCAPE_MODE_QUOTE,
    AV_ESCAPE_MODE_XML,
};
# 367 "./libavutil/avstring.h"
__attribute__((warn_unused_result))
int av_escape(char **dst, const char *src, const char *special_chars,
              enum AVEscapeMode mode, int flags);
# 407 "./libavutil/avstring.h"
__attribute__((warn_unused_result))
int av_utf8_decode(int32_t *codep, const uint8_t **bufp, const uint8_t *buf_end,
                   unsigned int flags);






int av_match_list(const char *name, const char *list, char separator);





int av_sscanf(const char *string, const char *format, ...);
# 31 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2
# 1 "./libavutil/channel_layout.h" 1
# 26 "./libavutil/channel_layout.h"
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 1 3 4
# 61 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/Availability.h" 1 3 4
# 172 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/Availability.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/AvailabilityVersions.h" 1 3 4
# 173 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/Availability.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/AvailabilityInternal.h" 1 3 4
# 176 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/AvailabilityInternal.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/AvailabilityInternalLegacy.h" 1 3 4
# 177 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/AvailabilityInternal.h" 2 3 4
# 174 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/Availability.h" 2 3 4
# 62 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4


# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types.h" 1 3 4
# 40 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_types.h" 3 4
typedef int __darwin_nl_item;
typedef int __darwin_wctrans_t;

typedef __uint32_t __darwin_wctype_t;
# 65 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 1 3 4
# 79 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 3 4
typedef enum {
 P_ALL,
 P_PID,
 P_PGID
} idtype_t;





# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_pid_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_pid_t.h" 3 4
typedef __darwin_pid_t pid_t;
# 90 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_id_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_id_t.h" 3 4
typedef __darwin_id_t id_t;
# 91 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 2 3 4
# 109 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 1 3 4
# 73 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/appleapiopts.h" 1 3 4
# 74 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 2 3 4








# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/signal.h" 1 3 4
# 34 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/signal.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/signal.h" 1 3 4
# 17 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/signal.h" 3 4
typedef int sig_atomic_t;
# 35 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/signal.h" 2 3 4
# 83 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 2 3 4
# 146 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/_mcontext.h" 1 3 4
# 34 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/_mcontext.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_mcontext.h" 1 3 4
# 36 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_mcontext.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/machine/_structs.h" 1 3 4
# 35 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/machine/_structs.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 1 3 4
# 41 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __darwin_arm_exception_state
{
 __uint32_t __exception;
 __uint32_t __fsr;
 __uint32_t __far;
};
# 59 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __darwin_arm_exception_state64
{
 __uint64_t __far;
 __uint32_t __esr;
 __uint32_t __exception;
};
# 77 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __darwin_arm_thread_state
{
 __uint32_t __r[13];
 __uint32_t __sp;
 __uint32_t __lr;
 __uint32_t __pc;
 __uint32_t __cpsr;
};
# 136 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __darwin_arm_thread_state64
{
 __uint64_t __x[29];
 __uint64_t __fp;
 __uint64_t __lr;
 __uint64_t __sp;
 __uint64_t __pc;
 __uint32_t __cpsr;
 __uint32_t __pad;
};
# 477 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __darwin_arm_vfp_state
{
 __uint32_t __r[64];
 __uint32_t __fpscr;
};
# 496 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __darwin_arm_neon_state64
{
 __uint128_t __v[32];
 __uint32_t __fpsr;
 __uint32_t __fpcr;
};

struct __darwin_arm_neon_state
{
 __uint128_t __v[16];
 __uint32_t __fpsr;
 __uint32_t __fpcr;
};
# 567 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __arm_pagein_state
{
 int __pagein_error;
};
# 604 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __arm_legacy_debug_state
{
 __uint32_t __bvr[16];
 __uint32_t __bcr[16];
 __uint32_t __wvr[16];
 __uint32_t __wcr[16];
};
# 627 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __darwin_arm_debug_state32
{
 __uint32_t __bvr[16];
 __uint32_t __bcr[16];
 __uint32_t __wvr[16];
 __uint32_t __wcr[16];
 __uint64_t __mdscr_el1;
};


struct __darwin_arm_debug_state64
{
 __uint64_t __bvr[16];
 __uint64_t __bcr[16];
 __uint64_t __wvr[16];
 __uint64_t __wcr[16];
 __uint64_t __mdscr_el1;
};
# 669 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/arm/_structs.h" 3 4
struct __darwin_arm_cpmu_state64
{
 __uint64_t __ctrs[16];
};
# 36 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/mach/machine/_structs.h" 2 3 4
# 37 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_mcontext.h" 2 3 4




struct __darwin_mcontext32
{
 struct __darwin_arm_exception_state __es;
 struct __darwin_arm_thread_state __ss;
 struct __darwin_arm_vfp_state __fs;
};
# 64 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_mcontext.h" 3 4
struct __darwin_mcontext64
{
 struct __darwin_arm_exception_state64 __es;
 struct __darwin_arm_thread_state64 __ss;
 struct __darwin_arm_neon_state64 __ns;
};
# 85 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_mcontext.h" 3 4
typedef struct __darwin_mcontext64 *mcontext_t;
# 35 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/_mcontext.h" 2 3 4
# 147 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 2 3 4

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_attr_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_pthread/_pthread_attr_t.h" 3 4
typedef __darwin_pthread_attr_t pthread_attr_t;
# 149 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 2 3 4

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_sigaltstack.h" 1 3 4
# 42 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_sigaltstack.h" 3 4
struct __darwin_sigaltstack
{
 void *ss_sp;
 __darwin_size_t ss_size;
 int ss_flags;
};
typedef struct __darwin_sigaltstack stack_t;
# 151 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_ucontext.h" 1 3 4
# 43 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_ucontext.h" 3 4
struct __darwin_ucontext
{
 int uc_onstack;
 __darwin_sigset_t uc_sigmask;
 struct __darwin_sigaltstack uc_stack;
 struct __darwin_ucontext *uc_link;
 __darwin_size_t uc_mcsize;
 struct __darwin_mcontext64 *uc_mcontext;



};


typedef struct __darwin_ucontext ucontext_t;
# 152 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 2 3 4


# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_sigset_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_sigset_t.h" 3 4
typedef __darwin_sigset_t sigset_t;
# 155 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_size_t.h" 1 3 4
# 156 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_uid_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_uid_t.h" 3 4
typedef __darwin_uid_t uid_t;
# 157 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 2 3 4

union sigval {

 int sival_int;
 void *sival_ptr;
};





struct sigevent {
 int sigev_notify;
 int sigev_signo;
 union sigval sigev_value;
 void (*sigev_notify_function)(union sigval);
 pthread_attr_t *sigev_notify_attributes;
};


typedef struct __siginfo {
 int si_signo;
 int si_errno;
 int si_code;
 pid_t si_pid;
 uid_t si_uid;
 int si_status;
 void *si_addr;
 union sigval si_value;
 long si_band;
 unsigned long __pad[7];
} siginfo_t;
# 269 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 3 4
union __sigaction_u {
 void (*__sa_handler)(int);
 void (*__sa_sigaction)(int, struct __siginfo *,
     void *);
};


struct __sigaction {
 union __sigaction_u __sigaction_u;
 void (*sa_tramp)(void *, int, int, siginfo_t *, void *);
 sigset_t sa_mask;
 int sa_flags;
};




struct sigaction {
 union __sigaction_u __sigaction_u;
 sigset_t sa_mask;
 int sa_flags;
};
# 331 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 3 4
typedef void (*sig_t)(int);
# 348 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 3 4
struct sigvec {
 void (*sv_handler)(int);
 int sv_mask;
 int sv_flags;
};
# 367 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 3 4
struct sigstack {
 char *ss_sp;
 int ss_onstack;
};
# 390 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/signal.h" 3 4
void(*signal(int, void (*)(int)))(int);
# 110 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/resource.h" 1 3 4
# 80 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/resource.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_timeval.h" 1 3 4
# 34 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_timeval.h" 3 4
struct timeval
{
 __darwin_time_t tv_sec;
 __darwin_suseconds_t tv_usec;
};
# 81 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/resource.h" 2 3 4








typedef __uint64_t rlim_t;
# 152 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/resource.h" 3 4
struct rusage {
 struct timeval ru_utime;
 struct timeval ru_stime;
# 163 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/resource.h" 3 4
 long ru_maxrss;

 long ru_ixrss;
 long ru_idrss;
 long ru_isrss;
 long ru_minflt;
 long ru_majflt;
 long ru_nswap;
 long ru_inblock;
 long ru_oublock;
 long ru_msgsnd;
 long ru_msgrcv;
 long ru_nsignals;
 long ru_nvcsw;
 long ru_nivcsw;


};
# 200 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/resource.h" 3 4
typedef void *rusage_info_t;

struct rusage_info_v0 {
 uint8_t ri_uuid[16];
 uint64_t ri_user_time;
 uint64_t ri_system_time;
 uint64_t ri_pkg_idle_wkups;
 uint64_t ri_interrupt_wkups;
 uint64_t ri_pageins;
 uint64_t ri_wired_size;
 uint64_t ri_resident_size;
 uint64_t ri_phys_footprint;
 uint64_t ri_proc_start_abstime;
 uint64_t ri_proc_exit_abstime;
};

struct rusage_info_v1 {
 uint8_t ri_uuid[16];
 uint64_t ri_user_time;
 uint64_t ri_system_time;
 uint64_t ri_pkg_idle_wkups;
 uint64_t ri_interrupt_wkups;
 uint64_t ri_pageins;
 uint64_t ri_wired_size;
 uint64_t ri_resident_size;
 uint64_t ri_phys_footprint;
 uint64_t ri_proc_start_abstime;
 uint64_t ri_proc_exit_abstime;
 uint64_t ri_child_user_time;
 uint64_t ri_child_system_time;
 uint64_t ri_child_pkg_idle_wkups;
 uint64_t ri_child_interrupt_wkups;
 uint64_t ri_child_pageins;
 uint64_t ri_child_elapsed_abstime;
};

struct rusage_info_v2 {
 uint8_t ri_uuid[16];
 uint64_t ri_user_time;
 uint64_t ri_system_time;
 uint64_t ri_pkg_idle_wkups;
 uint64_t ri_interrupt_wkups;
 uint64_t ri_pageins;
 uint64_t ri_wired_size;
 uint64_t ri_resident_size;
 uint64_t ri_phys_footprint;
 uint64_t ri_proc_start_abstime;
 uint64_t ri_proc_exit_abstime;
 uint64_t ri_child_user_time;
 uint64_t ri_child_system_time;
 uint64_t ri_child_pkg_idle_wkups;
 uint64_t ri_child_interrupt_wkups;
 uint64_t ri_child_pageins;
 uint64_t ri_child_elapsed_abstime;
 uint64_t ri_diskio_bytesread;
 uint64_t ri_diskio_byteswritten;
};

struct rusage_info_v3 {
 uint8_t ri_uuid[16];
 uint64_t ri_user_time;
 uint64_t ri_system_time;
 uint64_t ri_pkg_idle_wkups;
 uint64_t ri_interrupt_wkups;
 uint64_t ri_pageins;
 uint64_t ri_wired_size;
 uint64_t ri_resident_size;
 uint64_t ri_phys_footprint;
 uint64_t ri_proc_start_abstime;
 uint64_t ri_proc_exit_abstime;
 uint64_t ri_child_user_time;
 uint64_t ri_child_system_time;
 uint64_t ri_child_pkg_idle_wkups;
 uint64_t ri_child_interrupt_wkups;
 uint64_t ri_child_pageins;
 uint64_t ri_child_elapsed_abstime;
 uint64_t ri_diskio_bytesread;
 uint64_t ri_diskio_byteswritten;
 uint64_t ri_cpu_time_qos_default;
 uint64_t ri_cpu_time_qos_maintenance;
 uint64_t ri_cpu_time_qos_background;
 uint64_t ri_cpu_time_qos_utility;
 uint64_t ri_cpu_time_qos_legacy;
 uint64_t ri_cpu_time_qos_user_initiated;
 uint64_t ri_cpu_time_qos_user_interactive;
 uint64_t ri_billed_system_time;
 uint64_t ri_serviced_system_time;
};

struct rusage_info_v4 {
 uint8_t ri_uuid[16];
 uint64_t ri_user_time;
 uint64_t ri_system_time;
 uint64_t ri_pkg_idle_wkups;
 uint64_t ri_interrupt_wkups;
 uint64_t ri_pageins;
 uint64_t ri_wired_size;
 uint64_t ri_resident_size;
 uint64_t ri_phys_footprint;
 uint64_t ri_proc_start_abstime;
 uint64_t ri_proc_exit_abstime;
 uint64_t ri_child_user_time;
 uint64_t ri_child_system_time;
 uint64_t ri_child_pkg_idle_wkups;
 uint64_t ri_child_interrupt_wkups;
 uint64_t ri_child_pageins;
 uint64_t ri_child_elapsed_abstime;
 uint64_t ri_diskio_bytesread;
 uint64_t ri_diskio_byteswritten;
 uint64_t ri_cpu_time_qos_default;
 uint64_t ri_cpu_time_qos_maintenance;
 uint64_t ri_cpu_time_qos_background;
 uint64_t ri_cpu_time_qos_utility;
 uint64_t ri_cpu_time_qos_legacy;
 uint64_t ri_cpu_time_qos_user_initiated;
 uint64_t ri_cpu_time_qos_user_interactive;
 uint64_t ri_billed_system_time;
 uint64_t ri_serviced_system_time;
 uint64_t ri_logical_writes;
 uint64_t ri_lifetime_max_phys_footprint;
 uint64_t ri_instructions;
 uint64_t ri_cycles;
 uint64_t ri_billed_energy;
 uint64_t ri_serviced_energy;
 uint64_t ri_interval_max_phys_footprint;
 uint64_t ri_runnable_time;
};

struct rusage_info_v5 {
 uint8_t ri_uuid[16];
 uint64_t ri_user_time;
 uint64_t ri_system_time;
 uint64_t ri_pkg_idle_wkups;
 uint64_t ri_interrupt_wkups;
 uint64_t ri_pageins;
 uint64_t ri_wired_size;
 uint64_t ri_resident_size;
 uint64_t ri_phys_footprint;
 uint64_t ri_proc_start_abstime;
 uint64_t ri_proc_exit_abstime;
 uint64_t ri_child_user_time;
 uint64_t ri_child_system_time;
 uint64_t ri_child_pkg_idle_wkups;
 uint64_t ri_child_interrupt_wkups;
 uint64_t ri_child_pageins;
 uint64_t ri_child_elapsed_abstime;
 uint64_t ri_diskio_bytesread;
 uint64_t ri_diskio_byteswritten;
 uint64_t ri_cpu_time_qos_default;
 uint64_t ri_cpu_time_qos_maintenance;
 uint64_t ri_cpu_time_qos_background;
 uint64_t ri_cpu_time_qos_utility;
 uint64_t ri_cpu_time_qos_legacy;
 uint64_t ri_cpu_time_qos_user_initiated;
 uint64_t ri_cpu_time_qos_user_interactive;
 uint64_t ri_billed_system_time;
 uint64_t ri_serviced_system_time;
 uint64_t ri_logical_writes;
 uint64_t ri_lifetime_max_phys_footprint;
 uint64_t ri_instructions;
 uint64_t ri_cycles;
 uint64_t ri_billed_energy;
 uint64_t ri_serviced_energy;
 uint64_t ri_interval_max_phys_footprint;
 uint64_t ri_runnable_time;
 uint64_t ri_flags;
};

struct rusage_info_v6 {
 uint8_t ri_uuid[16];
 uint64_t ri_user_time;
 uint64_t ri_system_time;
 uint64_t ri_pkg_idle_wkups;
 uint64_t ri_interrupt_wkups;
 uint64_t ri_pageins;
 uint64_t ri_wired_size;
 uint64_t ri_resident_size;
 uint64_t ri_phys_footprint;
 uint64_t ri_proc_start_abstime;
 uint64_t ri_proc_exit_abstime;
 uint64_t ri_child_user_time;
 uint64_t ri_child_system_time;
 uint64_t ri_child_pkg_idle_wkups;
 uint64_t ri_child_interrupt_wkups;
 uint64_t ri_child_pageins;
 uint64_t ri_child_elapsed_abstime;
 uint64_t ri_diskio_bytesread;
 uint64_t ri_diskio_byteswritten;
 uint64_t ri_cpu_time_qos_default;
 uint64_t ri_cpu_time_qos_maintenance;
 uint64_t ri_cpu_time_qos_background;
 uint64_t ri_cpu_time_qos_utility;
 uint64_t ri_cpu_time_qos_legacy;
 uint64_t ri_cpu_time_qos_user_initiated;
 uint64_t ri_cpu_time_qos_user_interactive;
 uint64_t ri_billed_system_time;
 uint64_t ri_serviced_system_time;
 uint64_t ri_logical_writes;
 uint64_t ri_lifetime_max_phys_footprint;
 uint64_t ri_instructions;
 uint64_t ri_cycles;
 uint64_t ri_billed_energy;
 uint64_t ri_serviced_energy;
 uint64_t ri_interval_max_phys_footprint;
 uint64_t ri_runnable_time;
 uint64_t ri_flags;
 uint64_t ri_user_ptime;
 uint64_t ri_system_ptime;
 uint64_t ri_pinstructions;
 uint64_t ri_pcycles;
 uint64_t ri_energy_nj;
 uint64_t ri_penergy_nj;
 uint64_t ri_reserved[14];
};

typedef struct rusage_info_v6 rusage_info_current;
# 459 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/resource.h" 3 4
struct rlimit {
 rlim_t rlim_cur;
 rlim_t rlim_max;
};
# 494 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/resource.h" 3 4
struct proc_rlimit_control_wakeupmon {
 uint32_t wm_flags;
 int32_t wm_rate;
};
# 566 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/resource.h" 3 4
int getpriority(int, id_t);

int getiopolicy_np(int, int) __attribute__((availability(macosx,introduced=10.5)));

int getrlimit(int, struct rlimit *) __asm("_" "getrlimit" );
int getrusage(int, struct rusage *);
int setpriority(int, id_t, int);

int setiopolicy_np(int, int, int) __attribute__((availability(macosx,introduced=10.5)));

int setrlimit(int, const struct rlimit *) __asm("_" "setrlimit" );
# 111 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 2 3 4
# 186 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/endian.h" 1 3 4
# 37 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/endian.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/endian.h" 1 3 4
# 77 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/endian.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_endian.h" 1 3 4
# 94 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_endian.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/endian.h" 1 3 4
# 95 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_endian.h" 2 3 4
# 131 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_endian.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/_OSByteOrder.h" 1 3 4
# 80 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/_OSByteOrder.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/arm/OSByteOrder.h" 1 3 4








# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/arch.h" 1 3 4
# 10 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/arm/OSByteOrder.h" 2 3 4



static inline
uint16_t
_OSSwapInt16(
 uint16_t _data
 )
{

 return (uint16_t)(_data << 8 | _data >> 8);
}

static inline
uint32_t
_OSSwapInt32(
 uint32_t _data
 )
{

 _data = __builtin_bswap32(_data);





 return _data;
}

static inline
uint64_t
_OSSwapInt64(
 uint64_t _data
 )
{

 return __builtin_bswap64(_data);
# 60 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/arm/OSByteOrder.h" 3 4
}



struct _OSUnalignedU16 {
 volatile uint16_t __val;
} __attribute__((__packed__));

struct _OSUnalignedU32 {
 volatile uint32_t __val;
} __attribute__((__packed__));

struct _OSUnalignedU64 {
 volatile uint64_t __val;
} __attribute__((__packed__));
# 87 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/arm/OSByteOrder.h" 3 4
static inline
uint16_t
OSReadSwapInt16(
 const volatile void * _base,
 uintptr_t _offset
 )
{
 return _OSSwapInt16(((struct _OSUnalignedU16 *)((uintptr_t)_base + _offset))->__val);
}
# 109 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/arm/OSByteOrder.h" 3 4
static inline
uint32_t
OSReadSwapInt32(
 const volatile void * _base,
 uintptr_t _offset
 )
{
 return _OSSwapInt32(((struct _OSUnalignedU32 *)((uintptr_t)_base + _offset))->__val);
}
# 131 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/arm/OSByteOrder.h" 3 4
static inline
uint64_t
OSReadSwapInt64(
 const volatile void * _base,
 uintptr_t _offset
 )
{
 return _OSSwapInt64(((struct _OSUnalignedU64 *)((uintptr_t)_base + _offset))->__val);
}
# 156 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/arm/OSByteOrder.h" 3 4
static inline
void
OSWriteSwapInt16(
 volatile void * _base,
 uintptr_t _offset,
 uint16_t _data
 )
{
 ((struct _OSUnalignedU16 *)((uintptr_t)_base + _offset))->__val = _OSSwapInt16(_data);
}
# 180 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/arm/OSByteOrder.h" 3 4
static inline
void
OSWriteSwapInt32(
 volatile void * _base,
 uintptr_t _offset,
 uint32_t _data
 )
{
 ((struct _OSUnalignedU32 *)((uintptr_t)_base + _offset))->__val = _OSSwapInt32(_data);
}
# 204 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/arm/OSByteOrder.h" 3 4
static inline
void
OSWriteSwapInt64(
 volatile void * _base,
 uintptr_t _offset,
 uint64_t _data
 )
{
 ((struct _OSUnalignedU64 *)((uintptr_t)_base + _offset))->__val = _OSSwapInt64(_data);
}
# 81 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/libkern/_OSByteOrder.h" 2 3 4
# 132 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_endian.h" 2 3 4
# 78 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/endian.h" 2 3 4
# 38 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/endian.h" 2 3 4
# 187 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 2 3 4







union wait {
 int w_status;



 struct {

  unsigned int w_Termsig:7,
      w_Coredump:1,
      w_Retcode:8,
      w_Filler:16;







 } w_T;





 struct {

  unsigned int w_Stopval:8,
      w_Stopsig:8,
      w_Filler:16;






 } w_S;
};
# 248 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/wait.h" 3 4
pid_t wait(int *) __asm("_" "wait" );
pid_t waitpid(pid_t, int *, int) __asm("_" "waitpid" );

int waitid(idtype_t, id_t, siginfo_t *, int) __asm("_" "waitid" );


pid_t wait3(int *, int, struct rusage *);
pid_t wait4(pid_t, int *, int, struct rusage *);
# 67 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/alloca.h" 1 3 4
# 29 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/alloca.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_size_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/alloca.h" 2 3 4


void *alloca(size_t);
# 69 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4





# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_size_t.h" 1 3 4
# 75 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4


# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_ct_rune_t.h" 1 3 4
# 32 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_ct_rune_t.h" 3 4
typedef __darwin_ct_rune_t ct_rune_t;
# 78 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_rune_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_rune_t.h" 3 4
typedef __darwin_rune_t rune_t;
# 79 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4


# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_wchar_t.h" 1 3 4
# 82 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4

typedef struct {
 int quot;
 int rem;
} div_t;

typedef struct {
 long quot;
 long rem;
} ldiv_t;


typedef struct {
 long long quot;
 long long rem;
} lldiv_t;


# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_null.h" 1 3 4
# 101 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4
# 118 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 3 4
extern int __mb_cur_max;
# 128 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h" 1 3 4
# 36 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_size_t.h" 1 3 4
# 37 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h" 2 3 4

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/malloc/_malloc_type.h" 1 3 4
# 37 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/malloc/_malloc_type.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_size_t.h" 1 3 4
# 38 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/malloc/_malloc_type.h" 2 3 4








typedef unsigned long long malloc_type_id_t;

__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_malloc(size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(1)));
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_calloc(size_t count, size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(1,2)));
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void malloc_type_free(void *ptr, malloc_type_id_t type_id);
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_realloc(void *ptr, size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(2)));
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_valloc(size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(1)));
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_aligned_alloc(size_t alignment, size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(2)));
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) int malloc_type_posix_memalign(void **memptr, size_t alignment, size_t size, malloc_type_id_t type_id) ;




typedef struct _malloc_zone_t malloc_zone_t;

__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_zone_malloc(malloc_zone_t *zone, size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(2)));
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_zone_calloc(malloc_zone_t *zone, size_t count, size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(2,3)));
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void malloc_type_zone_free(malloc_zone_t *zone, void *ptr, malloc_type_id_t type_id);
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_zone_realloc(malloc_zone_t *zone, void *ptr, size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(3)));
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_zone_valloc(malloc_zone_t *zone, size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(2)));
__attribute__((availability(macos,unavailable))) __attribute__((availability(ios,unavailable))) __attribute__((availability(tvos,unavailable))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(visionos,unavailable))) void *malloc_type_zone_memalign(malloc_zone_t *zone, size_t alignment, size_t size, malloc_type_id_t type_id) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(3)));
# 39 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/malloc/_malloc.h" 2 3 4






void *malloc(size_t __size) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(1))) ;
void *calloc(size_t __count, size_t __size) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(1,2))) ;
void free(void *);
void *realloc(void *__ptr, size_t __size) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(2))) ;

void *valloc(size_t) __attribute__((alloc_size(1))) ;




void *aligned_alloc(size_t __alignment, size_t __size) __attribute__((__warn_unused_result__)) __attribute__((alloc_size(2))) __attribute__((availability(macosx,introduced=10.15))) __attribute__((availability(ios,introduced=13.0))) __attribute__((availability(tvos,introduced=13.0))) __attribute__((availability(watchos,introduced=6.0)));

int posix_memalign(void **__memptr, size_t __alignment, size_t __size) __attribute__((availability(macosx,introduced=10.6)));
# 129 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4


void abort(void) __attribute__((__cold__)) __attribute__((__noreturn__));
int abs(int) __attribute__((__const__));
int atexit(void (* _Nonnull)(void));
double atof(const char *);
int atoi(const char *);
long atol(const char *);

long long
  atoll(const char *);

void *bsearch(const void *__key, const void *__base, size_t __nel,
     size_t __width, int (* _Nonnull __compar)(const void *, const void *));

div_t div(int, int) __attribute__((__const__));
void exit(int) __attribute__((__noreturn__));

char *getenv(const char *);
long labs(long) __attribute__((__const__));
ldiv_t ldiv(long, long) __attribute__((__const__));

long long
  llabs(long long);
lldiv_t lldiv(long long, long long);


int mblen(const char *__s, size_t __n);
size_t mbstowcs(wchar_t * restrict , const char * restrict, size_t);
int mbtowc(wchar_t * restrict, const char * restrict, size_t);

void qsort(void *__base, size_t __nel, size_t __width,
     int (* _Nonnull __compar)(const void *, const void *));
int rand(void) __attribute__((__availability__(swift, unavailable, message="Use arc4random instead.")));

void srand(unsigned) __attribute__((__availability__(swift, unavailable, message="Use arc4random instead.")));
double strtod(const char *, char **) __asm("_" "strtod" );
float strtof(const char *, char **) __asm("_" "strtof" );
long strtol(const char *__str, char **__endptr, int __base);
long double
  strtold(const char *, char **);

long long
  strtoll(const char *__str, char **__endptr, int __base);

unsigned long
  strtoul(const char *__str, char **__endptr, int __base);

unsigned long long
  strtoull(const char *__str, char **__endptr, int __base);


__attribute__((__availability__(swift, unavailable, message="Use posix_spawn APIs or NSTask instead. (On iOS, process spawning is unavailable.)")))
__attribute__((availability(macos,introduced=10.0))) __attribute__((availability(ios,unavailable)))
__attribute__((availability(watchos,unavailable))) __attribute__((availability(tvos,unavailable)))
int system(const char *) __asm("_" "system" );


size_t wcstombs(char * restrict, const wchar_t * restrict, size_t);
int wctomb(char *, wchar_t);


void _Exit(int) __attribute__((__noreturn__));
long a64l(const char *);
double drand48(void);
char *ecvt(double, int, int *restrict, int *restrict);
double erand48(unsigned short[3]);
char *fcvt(double, int, int *restrict, int *restrict);
char *gcvt(double, int, char *);
int getsubopt(char **, char * const *, char **);
int grantpt(int);

char *initstate(unsigned, char *, size_t);



long jrand48(unsigned short[3]) __attribute__((__availability__(swift, unavailable, message="Use arc4random instead.")));
char *l64a(long);
void lcong48(unsigned short[7]);
long lrand48(void) __attribute__((__availability__(swift, unavailable, message="Use arc4random instead.")));

__attribute__((__deprecated__("This function is provided for compatibility reasons only.  Due to security concerns inherent in the design of mktemp(3), it is highly recommended that you use mkstemp(3) instead.")))

char *mktemp(char *);
int mkstemp(char *);
long mrand48(void) __attribute__((__availability__(swift, unavailable, message="Use arc4random instead.")));
long nrand48(unsigned short[3]) __attribute__((__availability__(swift, unavailable, message="Use arc4random instead.")));
int posix_openpt(int);
char *ptsname(int);


int ptsname_r(int fildes, char *buffer, size_t buflen) __attribute__((availability(macos,introduced=10.13.4))) __attribute__((availability(ios,introduced=11.3))) __attribute__((availability(tvos,introduced=11.3))) __attribute__((availability(watchos,introduced=4.3)));


int putenv(char *) __asm("_" "putenv" );
long random(void) __attribute__((__availability__(swift, unavailable, message="Use arc4random instead.")));
int rand_r(unsigned *) __attribute__((__availability__(swift, unavailable, message="Use arc4random instead.")));

char *realpath(const char * restrict, char * restrict) __asm("_" "realpath" "$DARWIN_EXTSN");



unsigned short
 *seed48(unsigned short[3]);
int setenv(const char * __name, const char * __value, int __overwrite) __asm("_" "setenv" );

void setkey(const char *) __asm("_" "setkey" );



char *setstate(const char *);
void srand48(long);

void srandom(unsigned);



int unlockpt(int);

int unsetenv(const char *) __asm("_" "unsetenv" );
# 257 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_dev_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_dev_t.h" 3 4
typedef __darwin_dev_t dev_t;
# 258 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_mode_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_mode_t.h" 3 4
typedef __darwin_mode_t mode_t;
# 259 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 2 3 4



uint32_t arc4random(void);
void arc4random_addrandom(unsigned char * , int )
    __attribute__((availability(macosx,introduced=10.0))) __attribute__((availability(macosx,deprecated=10.12,message="use arc4random_stir")))
    __attribute__((availability(ios,introduced=2.0))) __attribute__((availability(ios,deprecated=10.0,message="use arc4random_stir")))
    __attribute__((availability(tvos,introduced=2.0))) __attribute__((availability(tvos,deprecated=10.0,message="use arc4random_stir")))
    __attribute__((availability(watchos,introduced=1.0))) __attribute__((availability(watchos,deprecated=3.0,message="use arc4random_stir")));
void arc4random_buf(void * __buf, size_t __nbytes) __attribute__((availability(macosx,introduced=10.7)));
void arc4random_stir(void);
uint32_t
  arc4random_uniform(uint32_t __upper_bound) __attribute__((availability(macosx,introduced=10.7)));

int atexit_b(void (^ _Nonnull)(void)) __attribute__((availability(macosx,introduced=10.6)));
# 282 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 3 4
void *bsearch_b(const void *__key, const void *__base, size_t __nel,
     size_t __width, int (^ _Nonnull __compar)(const void *, const void *) __attribute__((__noescape__)))
     __attribute__((availability(macosx,introduced=10.6)));



char *cgetcap(char *, const char *, int);
int cgetclose(void);
int cgetent(char **, char **, const char *);
int cgetfirst(char **, char **);
int cgetmatch(const char *, const char *);
int cgetnext(char **, char **);
int cgetnum(char *, const char *, long *);
int cgetset(const char *);
int cgetstr(char *, const char *, char **);
int cgetustr(char *, const char *, char **);

int daemon(int, int) __asm("_" "daemon" ) __attribute__((availability(macosx,introduced=10.0,deprecated=10.5,message="Use posix_spawn APIs instead."))) __attribute__((availability(watchos,unavailable))) __attribute__((availability(tvos,unavailable)));
char *devname(dev_t, mode_t);
char *devname_r(dev_t, mode_t, char *buf, int len);
char *getbsize(int *, long *);
int getloadavg(double [], int);
const char
 *getprogname(void);
void setprogname(const char *);
# 316 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdlib.h" 3 4
int heapsort(void *__base, size_t __nel, size_t __width,
     int (* _Nonnull __compar)(const void *, const void *));

int heapsort_b(void *__base, size_t __nel, size_t __width,
     int (^ _Nonnull __compar)(const void *, const void *) __attribute__((__noescape__)))
     __attribute__((availability(macosx,introduced=10.6)));

int mergesort(void *__base, size_t __nel, size_t __width,
     int (* _Nonnull __compar)(const void *, const void *));

int mergesort_b(void *__base, size_t __nel, size_t __width,
     int (^ _Nonnull __compar)(const void *, const void *) __attribute__((__noescape__)))
     __attribute__((availability(macosx,introduced=10.6)));

void psort(void *__base, size_t __nel, size_t __width,
     int (* _Nonnull __compar)(const void *, const void *))
     __attribute__((availability(macosx,introduced=10.6)));

void psort_b(void *__base, size_t __nel, size_t __width,
     int (^ _Nonnull __compar)(const void *, const void *) __attribute__((__noescape__)))
     __attribute__((availability(macosx,introduced=10.6)));

void psort_r(void *__base, size_t __nel, size_t __width, void *,
     int (* _Nonnull __compar)(void *, const void *, const void *))
     __attribute__((availability(macosx,introduced=10.6)));

void qsort_b(void *__base, size_t __nel, size_t __width,
     int (^ _Nonnull __compar)(const void *, const void *) __attribute__((__noescape__)))
     __attribute__((availability(macosx,introduced=10.6)));

void qsort_r(void *__base, size_t __nel, size_t __width, void *,
     int (* _Nonnull __compar)(void *, const void *, const void *));
int radixsort(const unsigned char **__base, int __nel, const unsigned char *__table,
     unsigned __endbyte);
int rpmatch(const char *)
 __attribute__((availability(macos,introduced=10.15))) __attribute__((availability(ios,introduced=13.0))) __attribute__((availability(tvos,introduced=13.0))) __attribute__((availability(watchos,introduced=6.0)));
int sradixsort(const unsigned char **__base, int __nel, const unsigned char *__table,
     unsigned __endbyte);
void sranddev(void);
void srandomdev(void);
void *reallocf(void *__ptr, size_t __size) __attribute__((alloc_size(2)));
long long
 strtonum(const char *__numstr, long long __minval, long long __maxval, const char **__errstrp)
 __attribute__((availability(macos,introduced=11.0))) __attribute__((availability(ios,introduced=14.0))) __attribute__((availability(tvos,introduced=14.0))) __attribute__((availability(watchos,introduced=7.0)));

long long
  strtoq(const char *__str, char **__endptr, int __base);
unsigned long long
  strtouq(const char *__str, char **__endptr, int __base);

extern char *suboptarg;
# 27 "./libavutil/channel_layout.h" 2

# 1 "./libavutil/version.h" 1
# 30 "./libavutil/version.h"
# 1 "./libavutil/macros.h" 1
# 28 "./libavutil/macros.h"
# 1 "./libavutil/avconfig.h" 1
# 29 "./libavutil/macros.h" 2
# 31 "./libavutil/version.h" 2
# 29 "./libavutil/channel_layout.h" 2
# 47 "./libavutil/channel_layout.h"
enum AVChannel {

    AV_CHAN_NONE = -1,
    AV_CHAN_FRONT_LEFT,
    AV_CHAN_FRONT_RIGHT,
    AV_CHAN_FRONT_CENTER,
    AV_CHAN_LOW_FREQUENCY,
    AV_CHAN_BACK_LEFT,
    AV_CHAN_BACK_RIGHT,
    AV_CHAN_FRONT_LEFT_OF_CENTER,
    AV_CHAN_FRONT_RIGHT_OF_CENTER,
    AV_CHAN_BACK_CENTER,
    AV_CHAN_SIDE_LEFT,
    AV_CHAN_SIDE_RIGHT,
    AV_CHAN_TOP_CENTER,
    AV_CHAN_TOP_FRONT_LEFT,
    AV_CHAN_TOP_FRONT_CENTER,
    AV_CHAN_TOP_FRONT_RIGHT,
    AV_CHAN_TOP_BACK_LEFT,
    AV_CHAN_TOP_BACK_CENTER,
    AV_CHAN_TOP_BACK_RIGHT,

    AV_CHAN_STEREO_LEFT = 29,

    AV_CHAN_STEREO_RIGHT,
    AV_CHAN_WIDE_LEFT,
    AV_CHAN_WIDE_RIGHT,
    AV_CHAN_SURROUND_DIRECT_LEFT,
    AV_CHAN_SURROUND_DIRECT_RIGHT,
    AV_CHAN_LOW_FREQUENCY_2,
    AV_CHAN_TOP_SIDE_LEFT,
    AV_CHAN_TOP_SIDE_RIGHT,
    AV_CHAN_BOTTOM_FRONT_CENTER,
    AV_CHAN_BOTTOM_FRONT_LEFT,
    AV_CHAN_BOTTOM_FRONT_RIGHT,


    AV_CHAN_UNUSED = 0x200,


    AV_CHAN_UNKNOWN = 0x300,
# 101 "./libavutil/channel_layout.h"
    AV_CHAN_AMBISONIC_BASE = 0x400,


    AV_CHAN_AMBISONIC_END = 0x7ff,
};

enum AVChannelOrder {




    AV_CHANNEL_ORDER_UNSPEC,





    AV_CHANNEL_ORDER_NATIVE,






    AV_CHANNEL_ORDER_CUSTOM,
# 148 "./libavutil/channel_layout.h"
    AV_CHANNEL_ORDER_AMBISONIC,
};
# 250 "./libavutil/channel_layout.h"
enum AVMatrixEncoding {
    AV_MATRIX_ENCODING_NONE,
    AV_MATRIX_ENCODING_DOLBY,
    AV_MATRIX_ENCODING_DPLII,
    AV_MATRIX_ENCODING_DPLIIX,
    AV_MATRIX_ENCODING_DPLIIZ,
    AV_MATRIX_ENCODING_DOLBYEX,
    AV_MATRIX_ENCODING_DOLBYHEADPHONE,
    AV_MATRIX_ENCODING_NB
};
# 273 "./libavutil/channel_layout.h"
typedef struct AVChannelCustom {
    enum AVChannel id;
    char name[16];
    void *opaque;
} AVChannelCustom;
# 309 "./libavutil/channel_layout.h"
typedef struct AVChannelLayout {




    enum AVChannelOrder order;




    int nb_channels;






    union {
# 341 "./libavutil/channel_layout.h"
        uint64_t mask;
# 360 "./libavutil/channel_layout.h"
        AVChannelCustom *map;
    } u;




    void *opaque;
} AVChannelLayout;
# 431 "./libavutil/channel_layout.h"
struct AVBPrint;
# 458 "./libavutil/channel_layout.h"
__attribute__((deprecated))
uint64_t av_get_channel_layout(const char *name);
# 474 "./libavutil/channel_layout.h"
__attribute__((deprecated))
int av_get_extended_channel_layout(const char *name, uint64_t* channel_layout, int* nb_channels);
# 487 "./libavutil/channel_layout.h"
__attribute__((deprecated))
void av_get_channel_layout_string(char *buf, int buf_size, int nb_channels, uint64_t channel_layout);





__attribute__((deprecated))
void av_bprint_channel_layout(struct AVBPrint *bp, int nb_channels, uint64_t channel_layout);





__attribute__((deprecated))
int av_get_channel_layout_nb_channels(uint64_t channel_layout);






__attribute__((deprecated))
int64_t av_get_default_channel_layout(int nb_channels);
# 524 "./libavutil/channel_layout.h"
__attribute__((deprecated))
int av_get_channel_layout_channel_index(uint64_t channel_layout,
                                        uint64_t channel);





__attribute__((deprecated))
uint64_t av_channel_layout_extract_channel(uint64_t channel_layout, int index);
# 542 "./libavutil/channel_layout.h"
__attribute__((deprecated))
const char *av_get_channel_name(uint64_t channel);
# 552 "./libavutil/channel_layout.h"
__attribute__((deprecated))
const char *av_get_channel_description(uint64_t channel);
# 565 "./libavutil/channel_layout.h"
__attribute__((deprecated))
int av_get_standard_channel_layout(unsigned index, uint64_t *layout,
                                   const char **name);
# 584 "./libavutil/channel_layout.h"
int av_channel_name(char *buf, size_t buf_size, enum AVChannel channel);






void av_channel_name_bprint(struct AVBPrint *bp, enum AVChannel channel_id);
# 603 "./libavutil/channel_layout.h"
int av_channel_description(char *buf, size_t buf_size, enum AVChannel channel);






void av_channel_description_bprint(struct AVBPrint *bp, enum AVChannel channel_id);







enum AVChannel av_channel_from_string(const char *name);
# 630 "./libavutil/channel_layout.h"
int av_channel_layout_from_mask(AVChannelLayout *channel_layout, uint64_t mask);
# 649 "./libavutil/channel_layout.h"
int av_channel_layout_from_string(AVChannelLayout *channel_layout,
                                  const char *str);







void av_channel_layout_default(AVChannelLayout *ch_layout, int nb_channels);
# 669 "./libavutil/channel_layout.h"
const AVChannelLayout *av_channel_layout_standard(void **opaque);







void av_channel_layout_uninit(AVChannelLayout *channel_layout);
# 689 "./libavutil/channel_layout.h"
int av_channel_layout_copy(AVChannelLayout *dst, const AVChannelLayout *src);
# 704 "./libavutil/channel_layout.h"
int av_channel_layout_describe(const AVChannelLayout *channel_layout,
                               char *buf, size_t buf_size);







int av_channel_layout_describe_bprint(const AVChannelLayout *channel_layout,
                                      struct AVBPrint *bp);
# 725 "./libavutil/channel_layout.h"
enum AVChannel
av_channel_layout_channel_from_index(const AVChannelLayout *channel_layout, unsigned int idx);
# 737 "./libavutil/channel_layout.h"
int av_channel_layout_index_from_channel(const AVChannelLayout *channel_layout,
                                         enum AVChannel channel);
# 752 "./libavutil/channel_layout.h"
int av_channel_layout_index_from_string(const AVChannelLayout *channel_layout,
                                        const char *name);
# 767 "./libavutil/channel_layout.h"
enum AVChannel
av_channel_layout_channel_from_string(const AVChannelLayout *channel_layout,
                                      const char *name);
# 780 "./libavutil/channel_layout.h"
uint64_t av_channel_layout_subset(const AVChannelLayout *channel_layout,
                                  uint64_t mask);
# 790 "./libavutil/channel_layout.h"
int av_channel_layout_check(const AVChannelLayout *channel_layout);
# 805 "./libavutil/channel_layout.h"
int av_channel_layout_compare(const AVChannelLayout *chl, const AVChannelLayout *chl1);
# 32 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2
# 1 "./libavutil/common.h" 1
# 33 "./libavutil/common.h"
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/errno.h" 1 3 4
# 23 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/errno.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/errno.h" 1 3 4
# 76 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/errno.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_errno_t.h" 1 3 4
# 30 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_errno_t.h" 3 4
typedef int errno_t;
# 77 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/errno.h" 2 3 4



extern int * __error(void);
# 24 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/errno.h" 2 3 4
# 34 "./libavutil/common.h" 2
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/inttypes.h" 1 3
# 21 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/inttypes.h" 3
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/inttypes.h" 1 3 4
# 227 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/inttypes.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_wchar_t.h" 1 3 4
# 228 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/inttypes.h" 2 3 4






__attribute__((availability(macosx,introduced=10.4)))
extern intmax_t
imaxabs(intmax_t j);


typedef struct {
 intmax_t quot;
 intmax_t rem;
} imaxdiv_t;

__attribute__((availability(macosx,introduced=10.4)))
extern imaxdiv_t
imaxdiv(intmax_t __numer, intmax_t __denom);


__attribute__((availability(macosx,introduced=10.4)))
extern intmax_t
strtoimax(const char * restrict __nptr,
   char ** restrict __endptr,
   int __base);

__attribute__((availability(macosx,introduced=10.4)))
extern uintmax_t
strtoumax(const char * restrict __nptr,
   char ** restrict __endptr,
   int __base);


__attribute__((availability(macosx,introduced=10.4)))
extern intmax_t
wcstoimax(const wchar_t * restrict __nptr,
   wchar_t ** restrict __endptr,
   int __base);

__attribute__((availability(macosx,introduced=10.4)))
extern uintmax_t
wcstoumax(const wchar_t * restrict __nptr,
   wchar_t ** restrict __endptr,
   int __base);
# 22 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/inttypes.h" 2 3
# 35 "./libavutil/common.h" 2
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/limits.h" 1 3
# 21 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/limits.h" 3
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/limits.h" 1 3 4
# 64 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/limits.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/limits.h" 1 3 4
# 11 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/limits.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/limits.h" 1 3 4
# 45 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/limits.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/_limits.h" 1 3 4
# 46 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/arm/limits.h" 2 3 4
# 12 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/machine/limits.h" 2 3 4
# 65 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/limits.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/syslimits.h" 1 3 4
# 66 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/limits.h" 2 3 4
# 22 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/limits.h" 2 3
# 36 "./libavutil/common.h" 2
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 1 3 4
# 45 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
    typedef float float_t;
    typedef double double_t;
# 112 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
extern int __math_errhandling(void);
# 132 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
extern int __fpclassifyf(float);
extern int __fpclassifyd(double);
extern int __fpclassifyl(long double);
# 175 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
inline __attribute__ ((__always_inline__)) int __inline_isfinitef(float);
inline __attribute__ ((__always_inline__)) int __inline_isfinited(double);
inline __attribute__ ((__always_inline__)) int __inline_isfinitel(long double);
inline __attribute__ ((__always_inline__)) int __inline_isinff(float);
inline __attribute__ ((__always_inline__)) int __inline_isinfd(double);
inline __attribute__ ((__always_inline__)) int __inline_isinfl(long double);
inline __attribute__ ((__always_inline__)) int __inline_isnanf(float);
inline __attribute__ ((__always_inline__)) int __inline_isnand(double);
inline __attribute__ ((__always_inline__)) int __inline_isnanl(long double);
inline __attribute__ ((__always_inline__)) int __inline_isnormalf(float);
inline __attribute__ ((__always_inline__)) int __inline_isnormald(double);
inline __attribute__ ((__always_inline__)) int __inline_isnormall(long double);
inline __attribute__ ((__always_inline__)) int __inline_signbitf(float);
inline __attribute__ ((__always_inline__)) int __inline_signbitd(double);
inline __attribute__ ((__always_inline__)) int __inline_signbitl(long double);

inline __attribute__ ((__always_inline__)) int __inline_isfinitef(float __x) {
    return __x == __x && __builtin_fabsf(__x) != __builtin_inff();
}
inline __attribute__ ((__always_inline__)) int __inline_isfinited(double __x) {
    return __x == __x && __builtin_fabs(__x) != __builtin_inf();
}
inline __attribute__ ((__always_inline__)) int __inline_isfinitel(long double __x) {
    return __x == __x && __builtin_fabsl(__x) != __builtin_infl();
}
inline __attribute__ ((__always_inline__)) int __inline_isinff(float __x) {
    return __builtin_fabsf(__x) == __builtin_inff();
}
inline __attribute__ ((__always_inline__)) int __inline_isinfd(double __x) {
    return __builtin_fabs(__x) == __builtin_inf();
}
inline __attribute__ ((__always_inline__)) int __inline_isinfl(long double __x) {
    return __builtin_fabsl(__x) == __builtin_infl();
}
inline __attribute__ ((__always_inline__)) int __inline_isnanf(float __x) {
    return __x != __x;
}
inline __attribute__ ((__always_inline__)) int __inline_isnand(double __x) {
    return __x != __x;
}
inline __attribute__ ((__always_inline__)) int __inline_isnanl(long double __x) {
    return __x != __x;
}
inline __attribute__ ((__always_inline__)) int __inline_signbitf(float __x) {
    union { float __f; unsigned int __u; } __u;
    __u.__f = __x;
    return (int)(__u.__u >> 31);
}
inline __attribute__ ((__always_inline__)) int __inline_signbitd(double __x) {
    union { double __f; unsigned long long __u; } __u;
    __u.__f = __x;
    return (int)(__u.__u >> 63);
}
# 238 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
inline __attribute__ ((__always_inline__)) int __inline_signbitl(long double __x) {
    union { long double __f; unsigned long long __u;} __u;
    __u.__f = __x;
    return (int)(__u.__u >> 63);
}

inline __attribute__ ((__always_inline__)) int __inline_isnormalf(float __x) {
    return __inline_isfinitef(__x) && __builtin_fabsf(__x) >= 1.17549435e-38F;
}
inline __attribute__ ((__always_inline__)) int __inline_isnormald(double __x) {
    return __inline_isfinited(__x) && __builtin_fabs(__x) >= 2.2250738585072014e-308;
}
inline __attribute__ ((__always_inline__)) int __inline_isnormall(long double __x) {
    return __inline_isfinitel(__x) && __builtin_fabsl(__x) >= 2.2250738585072014e-308L;
}
# 309 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
extern float acosf(float);
extern double acos(double);
extern long double acosl(long double);

extern float asinf(float);
extern double asin(double);
extern long double asinl(long double);

extern float atanf(float);
extern double atan(double);
extern long double atanl(long double);

extern float atan2f(float, float);
extern double atan2(double, double);
extern long double atan2l(long double, long double);

extern float cosf(float);
extern double cos(double);
extern long double cosl(long double);

extern float sinf(float);
extern double sin(double);
extern long double sinl(long double);

extern float tanf(float);
extern double tan(double);
extern long double tanl(long double);

extern float acoshf(float);
extern double acosh(double);
extern long double acoshl(long double);

extern float asinhf(float);
extern double asinh(double);
extern long double asinhl(long double);

extern float atanhf(float);
extern double atanh(double);
extern long double atanhl(long double);

extern float coshf(float);
extern double cosh(double);
extern long double coshl(long double);

extern float sinhf(float);
extern double sinh(double);
extern long double sinhl(long double);

extern float tanhf(float);
extern double tanh(double);
extern long double tanhl(long double);

extern float expf(float);
extern double exp(double);
extern long double expl(long double);

extern float exp2f(float);
extern double exp2(double);
extern long double exp2l(long double);

extern float expm1f(float);
extern double expm1(double);
extern long double expm1l(long double);

extern float logf(float);
extern double log(double);
extern long double logl(long double);

extern float log10f(float);
extern double log10(double);
extern long double log10l(long double);

extern float log2f(float);
extern double log2(double);
extern long double log2l(long double);

extern float log1pf(float);
extern double log1p(double);
extern long double log1pl(long double);

extern float logbf(float);
extern double logb(double);
extern long double logbl(long double);

extern float modff(float, float *);
extern double modf(double, double *);
extern long double modfl(long double, long double *);

extern float ldexpf(float, int);
extern double ldexp(double, int);
extern long double ldexpl(long double, int);

extern float frexpf(float, int *);
extern double frexp(double, int *);
extern long double frexpl(long double, int *);

extern int ilogbf(float);
extern int ilogb(double);
extern int ilogbl(long double);

extern float scalbnf(float, int);
extern double scalbn(double, int);
extern long double scalbnl(long double, int);

extern float scalblnf(float, long int);
extern double scalbln(double, long int);
extern long double scalblnl(long double, long int);

extern float fabsf(float);
extern double fabs(double);
extern long double fabsl(long double);

extern float cbrtf(float);
extern double cbrt(double);
extern long double cbrtl(long double);

extern float hypotf(float, float);
extern double hypot(double, double);
extern long double hypotl(long double, long double);

extern float powf(float, float);
extern double pow(double, double);
extern long double powl(long double, long double);

extern float sqrtf(float);
extern double sqrt(double);
extern long double sqrtl(long double);

extern float erff(float);
extern double erf(double);
extern long double erfl(long double);

extern float erfcf(float);
extern double erfc(double);
extern long double erfcl(long double);




extern float lgammaf(float);
extern double lgamma(double);
extern long double lgammal(long double);

extern float tgammaf(float);
extern double tgamma(double);
extern long double tgammal(long double);

extern float ceilf(float);
extern double ceil(double);
extern long double ceill(long double);

extern float floorf(float);
extern double floor(double);
extern long double floorl(long double);

extern float nearbyintf(float);
extern double nearbyint(double);
extern long double nearbyintl(long double);

extern float rintf(float);
extern double rint(double);
extern long double rintl(long double);

extern long int lrintf(float);
extern long int lrint(double);
extern long int lrintl(long double);

extern float roundf(float);
extern double round(double);
extern long double roundl(long double);

extern long int lroundf(float);
extern long int lround(double);
extern long int lroundl(long double);




extern long long int llrintf(float);
extern long long int llrint(double);
extern long long int llrintl(long double);

extern long long int llroundf(float);
extern long long int llround(double);
extern long long int llroundl(long double);


extern float truncf(float);
extern double trunc(double);
extern long double truncl(long double);

extern float fmodf(float, float);
extern double fmod(double, double);
extern long double fmodl(long double, long double);

extern float remainderf(float, float);
extern double remainder(double, double);
extern long double remainderl(long double, long double);

extern float remquof(float, float, int *);
extern double remquo(double, double, int *);
extern long double remquol(long double, long double, int *);

extern float copysignf(float, float);
extern double copysign(double, double);
extern long double copysignl(long double, long double);

extern float nanf(const char *);
extern double nan(const char *);
extern long double nanl(const char *);

extern float nextafterf(float, float);
extern double nextafter(double, double);
extern long double nextafterl(long double, long double);

extern double nexttoward(double, long double);
extern float nexttowardf(float, long double);
extern long double nexttowardl(long double, long double);

extern float fdimf(float, float);
extern double fdim(double, double);
extern long double fdiml(long double, long double);

extern float fmaxf(float, float);
extern double fmax(double, double);
extern long double fmaxl(long double, long double);

extern float fminf(float, float);
extern double fmin(double, double);
extern long double fminl(long double, long double);

extern float fmaf(float, float, float);
extern double fma(double, double, double);
extern long double fmal(long double, long double, long double);
# 589 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
extern float __exp10f(float) __attribute__((availability(macos,introduced=10.9))) __attribute__((availability(ios,introduced=7.0)));
extern double __exp10(double) __attribute__((availability(macos,introduced=10.9))) __attribute__((availability(ios,introduced=7.0)));





inline __attribute__ ((__always_inline__)) void __sincosf(float __x, float *__sinp, float *__cosp);
inline __attribute__ ((__always_inline__)) void __sincos(double __x, double *__sinp, double *__cosp);
# 606 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
extern float __cospif(float) __attribute__((availability(macos,introduced=10.9))) __attribute__((availability(ios,introduced=7.0)));
extern double __cospi(double) __attribute__((availability(macos,introduced=10.9))) __attribute__((availability(ios,introduced=7.0)));
extern float __sinpif(float) __attribute__((availability(macos,introduced=10.9))) __attribute__((availability(ios,introduced=7.0)));
extern double __sinpi(double) __attribute__((availability(macos,introduced=10.9))) __attribute__((availability(ios,introduced=7.0)));
extern float __tanpif(float) __attribute__((availability(macos,introduced=10.9))) __attribute__((availability(ios,introduced=7.0)));
extern double __tanpi(double) __attribute__((availability(macos,introduced=10.9))) __attribute__((availability(ios,introduced=7.0)));
# 637 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
inline __attribute__ ((__always_inline__)) void __sincospif(float __x, float *__sinp, float *__cosp);
inline __attribute__ ((__always_inline__)) void __sincospi(double __x, double *__sinp, double *__cosp);






struct __float2 { float __sinval; float __cosval; };
struct __double2 { double __sinval; double __cosval; };

extern struct __float2 __sincosf_stret(float);
extern struct __double2 __sincos_stret(double);
extern struct __float2 __sincospif_stret(float);
extern struct __double2 __sincospi_stret(double);

inline __attribute__ ((__always_inline__)) void __sincosf(float __x, float *__sinp, float *__cosp) {
    const struct __float2 __stret = __sincosf_stret(__x);
    *__sinp = __stret.__sinval; *__cosp = __stret.__cosval;
}

inline __attribute__ ((__always_inline__)) void __sincos(double __x, double *__sinp, double *__cosp) {
    const struct __double2 __stret = __sincos_stret(__x);
    *__sinp = __stret.__sinval; *__cosp = __stret.__cosval;
}

inline __attribute__ ((__always_inline__)) void __sincospif(float __x, float *__sinp, float *__cosp) {
    const struct __float2 __stret = __sincospif_stret(__x);
    *__sinp = __stret.__sinval; *__cosp = __stret.__cosval;
}

inline __attribute__ ((__always_inline__)) void __sincospi(double __x, double *__sinp, double *__cosp) {
    const struct __double2 __stret = __sincospi_stret(__x);
    *__sinp = __stret.__sinval; *__cosp = __stret.__cosval;
}







extern double j0(double) __attribute__((availability(macos,introduced=10.0))) __attribute__((availability(ios,introduced=3.2)));
extern double j1(double) __attribute__((availability(macos,introduced=10.0))) __attribute__((availability(ios,introduced=3.2)));
extern double jn(int, double) __attribute__((availability(macos,introduced=10.0))) __attribute__((availability(ios,introduced=3.2)));
extern double y0(double) __attribute__((availability(macos,introduced=10.0))) __attribute__((availability(ios,introduced=3.2)));
extern double y1(double) __attribute__((availability(macos,introduced=10.0))) __attribute__((availability(ios,introduced=3.2)));
extern double yn(int, double) __attribute__((availability(macos,introduced=10.0))) __attribute__((availability(ios,introduced=3.2)));
extern double scalb(double, double);
extern int signgam;
# 764 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/math.h" 3 4
struct exception {
    int type;
    char *name;
    double arg1;
    double arg2;
    double retval;
};
# 37 "./libavutil/common.h" 2

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 1 3 4
# 64 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_stdio.h" 1 3 4
# 75 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_stdio.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_va_list.h" 1 3 4
# 32 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_va_list.h" 3 4
typedef __darwin_va_list va_list;
# 76 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_stdio.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_size_t.h" 1 3 4
# 77 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_stdio.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_null.h" 1 3 4
# 78 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_stdio.h" 2 3 4

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/stdio.h" 1 3 4
# 47 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/stdio.h" 3 4
int renameat(int, const char *, int, const char *) __attribute__((availability(macosx,introduced=10.10)));



int renamex_np(const char *, const char *, unsigned int) __attribute__((availability(macosx,introduced=10.12))) __attribute__((availability(ios,introduced=10.0))) __attribute__((availability(tvos,introduced=10.0))) __attribute__((availability(watchos,introduced=3.0)));
int renameatx_np(int, const char *, int, const char *, unsigned int) __attribute__((availability(macosx,introduced=10.12))) __attribute__((availability(ios,introduced=10.0))) __attribute__((availability(tvos,introduced=10.0))) __attribute__((availability(watchos,introduced=3.0)));
# 80 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_stdio.h" 2 3 4

typedef __darwin_off_t fpos_t;
# 92 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_stdio.h" 3 4
struct __sbuf {
 unsigned char *_base;
 int _size;
};


struct __sFILEX;
# 126 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_stdio.h" 3 4
typedef struct __sFILE {
 unsigned char *_p;
 int _r;
 int _w;
 short _flags;
 short _file;
 struct __sbuf _bf;
 int _lbfsize;


 void *_cookie;
 int (* _Nullable _close)(void *);
 int (* _Nullable _read) (void *, char *, int);
 fpos_t (* _Nullable _seek) (void *, fpos_t, int);
 int (* _Nullable _write)(void *, const char *, int);


 struct __sbuf _ub;
 struct __sFILEX *_extra;
 int _ur;


 unsigned char _ubuf[3];
 unsigned char _nbuf[1];


 struct __sbuf _lb;


 int _blksize;
 fpos_t _offset;
} FILE;
# 65 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 2 3 4

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_seek_set.h" 1 3 4
# 67 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 2 3 4


extern FILE *__stdinp;
extern FILE *__stdoutp;
extern FILE *__stderrp;
# 134 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
void clearerr(FILE *);
int fclose(FILE *);
int feof(FILE *);
int ferror(FILE *);
int fflush(FILE *);
int fgetc(FILE *);
int fgetpos(FILE * restrict, fpos_t *);
char *fgets(char * restrict, int, FILE *);



FILE *fopen(const char * restrict __filename, const char * restrict __mode) __asm("_" "fopen" );

int fprintf(FILE * restrict, const char * restrict, ...) __attribute__((__format__ (__printf__, 2, 3)));
int fputc(int, FILE *);
int fputs(const char * restrict, FILE * restrict) __asm("_" "fputs" );
size_t fread(void * restrict __ptr, size_t __size, size_t __nitems, FILE * restrict __stream);
FILE *freopen(const char * restrict, const char * restrict,
                 FILE * restrict) __asm("_" "freopen" );
int fscanf(FILE * restrict, const char * restrict, ...) __attribute__((__format__ (__scanf__, 2, 3)));
int fseek(FILE *, long, int);
int fsetpos(FILE *, const fpos_t *);
long ftell(FILE *);
size_t fwrite(const void * restrict __ptr, size_t __size, size_t __nitems, FILE * restrict __stream) __asm("_" "fwrite" );
int getc(FILE *);
int getchar(void);


__attribute__((__deprecated__("This function is provided for compatibility reasons only.  Due to security concerns inherent in the design of gets(3), it is highly recommended that you use fgets(3) instead.")))

char *gets(char *);

void perror(const char *) __attribute__((__cold__));
int printf(const char * restrict, ...) __attribute__((__format__ (__printf__, 1, 2)));
int putc(int, FILE *);
int putchar(int);
int puts(const char *);
int remove(const char *);
int rename (const char *__old, const char *__new);
void rewind(FILE *);
int scanf(const char * restrict, ...) __attribute__((__format__ (__scanf__, 1, 2)));
void setbuf(FILE * restrict, char * restrict);
int setvbuf(FILE * restrict, char * restrict, int, size_t);

__attribute__((__availability__(swift, unavailable, message="Use snprintf instead.")))

__attribute__((__deprecated__("This function is provided for compatibility reasons only.  Due to security concerns inherent in the design of sprintf(3), it is highly recommended that you use snprintf(3) instead.")))

int sprintf(char * restrict, const char * restrict, ...) __attribute__((__format__ (__printf__, 2, 3)));

int sscanf(const char * restrict, const char * restrict, ...) __attribute__((__format__ (__scanf__, 2, 3)));
FILE *tmpfile(void);

__attribute__((__availability__(swift, unavailable, message="Use mkstemp(3) instead.")))

__attribute__((__deprecated__("This function is provided for compatibility reasons only.  Due to security concerns inherent in the design of tmpnam(3), it is highly recommended that you use mkstemp(3) instead.")))

char *tmpnam(char *);

int ungetc(int, FILE *);
int vfprintf(FILE * restrict, const char * restrict, va_list) __attribute__((__format__ (__printf__, 2, 0)));
int vprintf(const char * restrict, va_list) __attribute__((__format__ (__printf__, 1, 0)));

__attribute__((__availability__(swift, unavailable, message="Use vsnprintf instead.")))

__attribute__((__deprecated__("This function is provided for compatibility reasons only.  Due to security concerns inherent in the design of sprintf(3), it is highly recommended that you use vsnprintf(3) instead.")))

int vsprintf(char * restrict, const char * restrict, va_list) __attribute__((__format__ (__printf__, 2, 0)));
# 213 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_ctermid.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/_ctermid.h" 3 4
char *ctermid(char *);
# 214 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 2 3 4






FILE *fdopen(int, const char *) __asm("_" "fdopen" );

int fileno(FILE *);
# 233 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
int pclose(FILE *) __attribute__((__availability__(swift, unavailable, message="Use posix_spawn APIs or NSTask instead. (On iOS, process spawning is unavailable.)")));



FILE *popen(const char *, const char *) __asm("_" "popen" ) __attribute__((__availability__(swift, unavailable, message="Use posix_spawn APIs or NSTask instead. (On iOS, process spawning is unavailable.)")));
# 252 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
int __srget(FILE *);
int __svfscanf(FILE *, const char *, va_list) __attribute__((__format__ (__scanf__, 2, 0)));
int __swbuf(int, FILE *);
# 263 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
inline __attribute__ ((__always_inline__)) int __sputc(int _c, FILE *_p) {
 if (--_p->_w >= 0 || (_p->_w >= _p->_lbfsize && (char)_c != '\n'))
  return (*_p->_p++ = _c);
 else
  return (__swbuf(_c, _p));
}
# 289 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
void flockfile(FILE *);
int ftrylockfile(FILE *);
void funlockfile(FILE *);
int getc_unlocked(FILE *);
int getchar_unlocked(void);
int putc_unlocked(int, FILE *);
int putchar_unlocked(int);



int getw(FILE *);
int putw(int, FILE *);


__attribute__((__availability__(swift, unavailable, message="Use mkstemp(3) instead.")))

__attribute__((__deprecated__("This function is provided for compatibility reasons only.  Due to security concerns inherent in the design of tempnam(3), it is highly recommended that you use mkstemp(3) instead.")))

char *tempnam(const char *__dir, const char *__prefix) __asm("_" "tempnam" );
# 327 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_off_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_off_t.h" 3 4
typedef __darwin_off_t off_t;
# 328 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 2 3 4


int fseeko(FILE * __stream, off_t __offset, int __whence);
off_t ftello(FILE * __stream);





int snprintf(char * restrict __str, size_t __size, const char * restrict __format, ...) __attribute__((__format__ (__printf__, 3, 4)));
int vfscanf(FILE * restrict __stream, const char * restrict __format, va_list) __attribute__((__format__ (__scanf__, 2, 0)));
int vscanf(const char * restrict __format, va_list) __attribute__((__format__ (__scanf__, 1, 0)));
int vsnprintf(char * restrict __str, size_t __size, const char * restrict __format, va_list) __attribute__((__format__ (__printf__, 3, 0)));
int vsscanf(const char * restrict __str, const char * restrict __format, va_list) __attribute__((__format__ (__scanf__, 2, 0)));
# 352 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_ssize_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_ssize_t.h" 3 4
typedef __darwin_ssize_t ssize_t;
# 353 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 2 3 4


int dprintf(int, const char * restrict, ...) __attribute__((__format__ (__printf__, 2, 3))) __attribute__((availability(macosx,introduced=10.7)));
int vdprintf(int, const char * restrict, va_list) __attribute__((__format__ (__printf__, 2, 0))) __attribute__((availability(macosx,introduced=10.7)));
ssize_t getdelim(char ** restrict __linep, size_t * restrict __linecapp, int __delimiter, FILE * restrict __stream) __attribute__((availability(macosx,introduced=10.7)));
ssize_t getline(char ** restrict __linep, size_t * restrict __linecapp, FILE * restrict __stream) __attribute__((availability(macosx,introduced=10.7)));
FILE *fmemopen(void * restrict __buf, size_t __size, const char * restrict __mode) __attribute__((availability(macos,introduced=10.13))) __attribute__((availability(ios,introduced=11.0))) __attribute__((availability(tvos,introduced=11.0))) __attribute__((availability(watchos,introduced=4.0)));
FILE *open_memstream(char **__bufp, size_t *__sizep) __attribute__((availability(macos,introduced=10.13))) __attribute__((availability(ios,introduced=11.0))) __attribute__((availability(tvos,introduced=11.0))) __attribute__((availability(watchos,introduced=4.0)));
# 370 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
extern const int sys_nerr;
extern const char *const sys_errlist[];

int asprintf(char ** restrict, const char * restrict, ...) __attribute__((__format__ (__printf__, 2, 3)));
char *ctermid_r(char *);
char *fgetln(FILE *, size_t *);
const char *fmtcheck(const char *, const char *) __attribute__((format_arg(2)));
int fpurge(FILE *);
void setbuffer(FILE *, char *, int);
int setlinebuf(FILE *);
int vasprintf(char ** restrict, const char * restrict, va_list) __attribute__((__format__ (__printf__, 2, 0)));





FILE *funopen(const void *,
                 int (* _Nullable)(void *, char *, int),
                 int (* _Nullable)(void *, const char *, int),
                 fpos_t (* _Nullable)(void *, fpos_t, int),
                 int (* _Nullable)(void *));
# 409 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/secure/_stdio.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/secure/_stdio.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/secure/_common.h" 1 3 4
# 32 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/secure/_stdio.h" 2 3 4
# 42 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/secure/_stdio.h" 3 4
extern int __sprintf_chk (char * restrict, int, size_t,
     const char * restrict, ...);
# 52 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/secure/_stdio.h" 3 4
extern int __snprintf_chk (char * restrict, size_t, int, size_t,
      const char * restrict, ...);







extern int __vsprintf_chk (char * restrict, int, size_t,
      const char * restrict, va_list);







extern int __vsnprintf_chk (char * restrict, size_t, int, size_t,
       const char * restrict, va_list);
# 410 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/stdio.h" 2 3 4
# 39 "./libavutil/common.h" 2

# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 1 3 4
# 64 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_size_t.h" 1 3 4
# 65 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 2 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_null.h" 1 3 4
# 66 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 2 3 4




void *memchr(const void *__s, int __c, size_t __n);
int memcmp(const void *__s1, const void *__s2, size_t __n);
void *memcpy(void *__dst, const void *__src, size_t __n);
void *memmove(void *__dst, const void *__src, size_t __len);
void *memset(void *__b, int __c, size_t __len);
char *strcat(char *__s1, const char *__s2);
char *strchr(const char *__s, int __c);
int strcmp(const char *__s1, const char *__s2);
int strcoll(const char *__s1, const char *__s2);
char *strcpy(char *__dst, const char *__src);
size_t strcspn(const char *__s, const char *__charset);
char *strerror(int __errnum) __asm("_" "strerror" );
size_t strlen(const char *__s);
char *strncat(char *__s1, const char *__s2, size_t __n);
int strncmp(const char *__s1, const char *__s2, size_t __n);
char *strncpy(char *__dst, const char *__src, size_t __n);
char *strpbrk(const char *__s, const char *__charset);
char *strrchr(const char *__s, int __c);
size_t strspn(const char *__s, const char *__charset);
char *strstr(const char *__big, const char *__little);
char *strtok(char *__str, const char *__sep);
size_t strxfrm(char *__s1, const char *__s2, size_t __n);
# 104 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 3 4
char *strtok_r(char *__str, const char *__sep, char **__lasts);
# 116 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 3 4
int strerror_r(int __errnum, char *__strerrbuf, size_t __buflen);
char *strdup(const char *__s1);
void *memccpy(void *__dst, const void *__src, int __c, size_t __n);
# 130 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 3 4
char *stpcpy(char *__dst, const char *__src);
char *stpncpy(char *__dst, const char *__src, size_t __n) __attribute__((availability(macosx,introduced=10.7)));
char *strndup(const char *__s1, size_t __n) __attribute__((availability(macosx,introduced=10.7)));
size_t strnlen(const char *__s1, size_t __n) __attribute__((availability(macosx,introduced=10.7)));
char *strsignal(int __sig);






# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_rsize_t.h" 1 3 4
# 31 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_rsize_t.h" 3 4
typedef __darwin_size_t rsize_t;
# 142 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 2 3 4



errno_t memset_s(void *__s, rsize_t __smax, int __c, rsize_t __n) __attribute__((availability(macosx,introduced=10.9)));
# 155 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 3 4
void *memmem(const void *__big, size_t __big_len, const void *__little, size_t __little_len) __attribute__((availability(macosx,introduced=10.7)));
void memset_pattern4(void *__b, const void *__pattern4, size_t __len) __attribute__((availability(macosx,introduced=10.5)));
void memset_pattern8(void *__b, const void *__pattern8, size_t __len) __attribute__((availability(macosx,introduced=10.5)));
void memset_pattern16(void *__b, const void *__pattern16, size_t __len) __attribute__((availability(macosx,introduced=10.5)));

char *strcasestr(const char *__big, const char *__little);
char *strnstr(const char *__big, const char *__little, size_t __len);
size_t strlcat(char *__dst, const char *__source, size_t __size);
size_t strlcpy(char *__dst, const char *__source, size_t __size);
void strmode(int __mode, char *__bp);
char *strsep(char **__stringp, const char *__delim);


void swab(const void * restrict, void * restrict, ssize_t);

__attribute__((availability(macosx,introduced=10.12.1))) __attribute__((availability(ios,introduced=10.1)))
__attribute__((availability(tvos,introduced=10.0.1))) __attribute__((availability(watchos,introduced=3.1)))
int timingsafe_bcmp(const void *__b1, const void *__b2, size_t __len);

__attribute__((availability(macosx,introduced=11.0))) __attribute__((availability(ios,introduced=14.0)))
__attribute__((availability(tvos,introduced=14.0))) __attribute__((availability(watchos,introduced=7.0)))
int strsignal_r(int __sig, char *__strsignalbuf, size_t __buflen);







# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/strings.h" 1 3 4
# 65 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/strings.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/sys/_types/_size_t.h" 1 3 4
# 66 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/strings.h" 2 3 4




int bcmp(const void *, const void *, size_t) ;
void bcopy(const void *, void *, size_t) ;
void bzero(void *, size_t) ;
char *index(const char *, int) ;
char *rindex(const char *, int) ;


int ffs(int);
int strcasecmp(const char *, const char *);
int strncasecmp(const char *, const char *, size_t);





int ffsl(long) __attribute__((availability(macosx,introduced=10.5)));
int ffsll(long long) __attribute__((availability(macosx,introduced=10.9)));
int fls(int) __attribute__((availability(macosx,introduced=10.5)));
int flsl(long) __attribute__((availability(macosx,introduced=10.5)));
int flsll(long long) __attribute__((availability(macosx,introduced=10.9)));


# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 1 3 4
# 93 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/strings.h" 2 3 4




# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/secure/_strings.h" 1 3 4
# 98 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/strings.h" 2 3 4
# 185 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 2 3 4
# 194 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 3 4
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/secure/_string.h" 1 3 4
# 195 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/string.h" 2 3 4
# 41 "./libavutil/common.h" 2


# 1 "./libavutil/error.h" 1
# 27 "./libavutil/error.h"
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/errno.h" 1 3 4
# 28 "./libavutil/error.h" 2
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 29 "./libavutil/error.h" 2
# 99 "./libavutil/error.h"
int av_strerror(int errnum, char *errbuf, size_t errbuf_size);
# 111 "./libavutil/error.h"
static inline char *av_make_error_string(char *errbuf, size_t errbuf_size, int errnum)
{
    av_strerror(errnum, errbuf, errbuf_size);
    return errbuf;
}
# 44 "./libavutil/common.h" 2
# 160 "./libavutil/common.h"
__attribute__((const)) int av_log2(unsigned v);



__attribute__((const)) int av_log2_16bit(unsigned v);
# 174 "./libavutil/common.h"
static __attribute__((always_inline)) inline __attribute__((const)) int av_clip_c(int a, int amin, int amax)
{



    if (a < amin) return amin;
    else if (a > amax) return amax;
    else return a;
}
# 191 "./libavutil/common.h"
static __attribute__((always_inline)) inline __attribute__((const)) int64_t av_clip64_c(int64_t a, int64_t amin, int64_t amax)
{



    if (a < amin) return amin;
    else if (a > amax) return amax;
    else return a;
}






static __attribute__((always_inline)) inline __attribute__((const)) uint8_t av_clip_uint8_c(int a)
{
    if (a&(~0xFF)) return (~a)>>31;
    else return a;
}






static __attribute__((always_inline)) inline __attribute__((const)) int8_t av_clip_int8_c(int a)
{
    if ((a+0x80U) & ~0xFF) return (a>>31) ^ 0x7F;
    else return a;
}






static __attribute__((always_inline)) inline __attribute__((const)) uint16_t av_clip_uint16_c(int a)
{
    if (a&(~0xFFFF)) return (~a)>>31;
    else return a;
}






static __attribute__((always_inline)) inline __attribute__((const)) int16_t av_clip_int16_c(int a)
{
    if ((a+0x8000U) & ~0xFFFF) return (a>>31) ^ 0x7FFF;
    else return a;
}






static __attribute__((always_inline)) inline __attribute__((const)) int32_t av_clipl_int32_c(int64_t a)
{
    if ((a+0x80000000u) & ~(0xFFFFFFFFULL)) return (int32_t)((a>>63) ^ 0x7FFFFFFF);
    else return (int32_t)a;
}







static __attribute__((always_inline)) inline __attribute__((const)) int av_clip_intp2_c(int a, int p)
{
    if (((unsigned)a + (1 << p)) & ~((2 << p) - 1))
        return (a >> 31) ^ ((1 << p) - 1);
    else
        return a;
}







static __attribute__((always_inline)) inline __attribute__((const)) unsigned av_clip_uintp2_c(int a, int p)
{
    if (a & ~((1<<p) - 1)) return (~a) >> 31 & ((1<<p) - 1);
    else return a;
}







static __attribute__((always_inline)) inline __attribute__((const)) unsigned av_mod_uintp2_c(unsigned a, unsigned p)
{
    return a & ((1U << p) - 1);
}
# 300 "./libavutil/common.h"
static __attribute__((always_inline)) inline int av_sat_add32_c(int a, int b)
{
    return av_clipl_int32_c((int64_t)a + b);
}
# 312 "./libavutil/common.h"
static __attribute__((always_inline)) inline int av_sat_dadd32_c(int a, int b)
{
    return av_sat_add32_c(a, av_sat_add32_c(b, b));
}
# 324 "./libavutil/common.h"
static __attribute__((always_inline)) inline int av_sat_sub32_c(int a, int b)
{
    return av_clipl_int32_c((int64_t)a - b);
}
# 336 "./libavutil/common.h"
static __attribute__((always_inline)) inline int av_sat_dsub32_c(int a, int b)
{
    return av_sat_sub32_c(a, av_sat_add32_c(b, b));
}
# 348 "./libavutil/common.h"
static __attribute__((always_inline)) inline int64_t av_sat_add64_c(int64_t a, int64_t b) {

    int64_t tmp;
    return !__builtin_add_overflow(a, b, &tmp) ? tmp : (tmp < 0 ? 9223372036854775807LL : (-9223372036854775807LL -1));






}
# 367 "./libavutil/common.h"
static __attribute__((always_inline)) inline int64_t av_sat_sub64_c(int64_t a, int64_t b) {

    int64_t tmp;
    return !__builtin_sub_overflow(a, b, &tmp) ? tmp : (tmp < 0 ? 9223372036854775807LL : (-9223372036854775807LL -1));







}
# 389 "./libavutil/common.h"
static __attribute__((always_inline)) inline __attribute__((const)) float av_clipf_c(float a, float amin, float amax)
{



    return ((((a) > (amin) ? (a) : (amin))) > (amax) ? (amax) : (((a) > (amin) ? (a) : (amin))));
}
# 406 "./libavutil/common.h"
static __attribute__((always_inline)) inline __attribute__((const)) double av_clipd_c(double a, double amin, double amax)
{



    return ((((a) > (amin) ? (a) : (amin))) > (amax) ? (amax) : (((a) > (amin) ? (a) : (amin))));
}





static __attribute__((always_inline)) inline __attribute__((const)) int av_ceil_log2_c(int x)
{
    return av_log2((x - 1U) << 1);
}






static __attribute__((always_inline)) inline __attribute__((const)) int av_popcount_c(uint32_t x)
{
    x -= (x >> 1) & 0x55555555;
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
    x = (x + (x >> 4)) & 0x0F0F0F0F;
    x += x >> 8;
    return (x + (x >> 16)) & 0x3F;
}






static __attribute__((always_inline)) inline __attribute__((const)) int av_popcount64_c(uint64_t x)
{
    return av_popcount_c((uint32_t)x) + av_popcount_c((uint32_t)(x >> 32));
}

static __attribute__((always_inline)) inline __attribute__((const)) int av_parity_c(uint32_t v)
{
    return av_popcount_c(v) & 1;
}
# 573 "./libavutil/common.h"
# 1 "./libavutil/mem.h" 1
# 30 "./libavutil/mem.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 31 "./libavutil/mem.h" 2
# 119 "./libavutil/mem.h"
void *av_malloc(size_t size) __attribute__((__malloc__)) ;
# 130 "./libavutil/mem.h"
void *av_mallocz(size_t size) __attribute__((__malloc__)) ;
# 143 "./libavutil/mem.h"
                    void *av_malloc_array(size_t nmemb, size_t size);
# 158 "./libavutil/mem.h"
void *av_calloc(size_t nmemb, size_t size) __attribute__((__malloc__)) ;
# 180 "./libavutil/mem.h"
void *av_realloc(void *ptr, size_t size) ;
# 201 "./libavutil/mem.h"
__attribute__((warn_unused_result))
int av_reallocp(void *ptr, size_t size);
# 219 "./libavutil/mem.h"
void *av_realloc_f(void *ptr, size_t nelem, size_t elsize);
# 239 "./libavutil/mem.h"
                    void *av_realloc_array(void *ptr, size_t nmemb, size_t size);
# 257 "./libavutil/mem.h"
int av_reallocp_array(void *ptr, size_t nmemb, size_t size);
# 291 "./libavutil/mem.h"
void *av_fast_realloc(void *ptr, unsigned int *size, size_t min_size);
# 322 "./libavutil/mem.h"
void av_fast_malloc(void *ptr, unsigned int *size, size_t min_size);
# 342 "./libavutil/mem.h"
void av_fast_mallocz(void *ptr, unsigned int *size, size_t min_size);
# 355 "./libavutil/mem.h"
void av_free(void *ptr);
# 378 "./libavutil/mem.h"
void av_freep(void *ptr);
# 388 "./libavutil/mem.h"
char *av_strdup(const char *s) __attribute__((__malloc__));
# 399 "./libavutil/mem.h"
char *av_strndup(const char *s, size_t len) __attribute__((__malloc__));
# 409 "./libavutil/mem.h"
void *av_memdup(const void *p, size_t size);
# 422 "./libavutil/mem.h"
void av_memcpy_backptr(uint8_t *dst, int back, int cnt);
# 524 "./libavutil/mem.h"
void av_dynarray_add(void *tab_ptr, int *nb_ptr, void *elem);
# 536 "./libavutil/mem.h"
__attribute__((warn_unused_result))
int av_dynarray_add_nofree(void *tab_ptr, int *nb_ptr, void *elem);
# 562 "./libavutil/mem.h"
void *av_dynarray2_add(void **tab_ptr, int *nb_ptr, size_t elem_size,
                       const uint8_t *elem_data);
# 585 "./libavutil/mem.h"
int av_size_mult(size_t a, size_t b, size_t *r);
# 600 "./libavutil/mem.h"
void av_max_alloc(size_t max);
# 574 "./libavutil/common.h" 2
# 33 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2
# 1 "./libavutil/float_dsp.h" 1
# 22 "./libavutil/float_dsp.h"
# 1 "./config.h" 1
# 23 "./libavutil/float_dsp.h" 2

typedef struct AVFloatDSPContext {
# 38 "./libavutil/float_dsp.h"
    void (*vector_fmul)(float *dst, const float *src0, const float *src1,
                        int len);
# 54 "./libavutil/float_dsp.h"
    void (*vector_fmac_scalar)(float *dst, const float *src, float mul,
                               int len);
# 70 "./libavutil/float_dsp.h"
    void (*vector_dmac_scalar)(double *dst, const double *src, double mul,
                               int len);
# 85 "./libavutil/float_dsp.h"
    void (*vector_fmul_scalar)(float *dst, const float *src, float mul,
                               int len);
# 100 "./libavutil/float_dsp.h"
    void (*vector_dmul_scalar)(double *dst, const double *src, double mul,
                               int len);
# 119 "./libavutil/float_dsp.h"
    void (*vector_fmul_window)(float *dst, const float *src0,
                               const float *src1, const float *win, int len);
# 137 "./libavutil/float_dsp.h"
    void (*vector_fmul_add)(float *dst, const float *src0, const float *src1,
                            const float *src2, int len);
# 154 "./libavutil/float_dsp.h"
    void (*vector_fmul_reverse)(float *dst, const float *src0,
                                const float *src1, int len);
# 164 "./libavutil/float_dsp.h"
    void (*butterflies_float)(float *restrict v1, float *restrict v2, int len);
# 175 "./libavutil/float_dsp.h"
    float (*scalarproduct_float)(const float *v1, const float *v2, int len);
# 190 "./libavutil/float_dsp.h"
    void (*vector_dmul)(double *dst, const double *src0, const double *src1,
                        int len);
} AVFloatDSPContext;
# 203 "./libavutil/float_dsp.h"
float avpriv_scalarproduct_float_c(const float *v1, const float *v2, int len);

void ff_float_dsp_init_aarch64(AVFloatDSPContext *fdsp);
void ff_float_dsp_init_arm(AVFloatDSPContext *fdsp);
void ff_float_dsp_init_ppc(AVFloatDSPContext *fdsp, int strict);
void ff_float_dsp_init_riscv(AVFloatDSPContext *fdsp);
void ff_float_dsp_init_x86(AVFloatDSPContext *fdsp);
void ff_float_dsp_init_mips(AVFloatDSPContext *fdsp);






AVFloatDSPContext *avpriv_float_dsp_alloc(int strict);
# 34 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2
# 1 "./libavutil/frame.h" 1
# 28 "./libavutil/frame.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 29 "./libavutil/frame.h" 2


# 1 "./libavutil/avutil.h" 1
# 171 "./libavutil/avutil.h"
unsigned avutil_version(void);






const char *av_version_info(void);




const char *avutil_configuration(void);




const char *avutil_license(void);
# 199 "./libavutil/avutil.h"
enum AVMediaType {
    AVMEDIA_TYPE_UNKNOWN = -1,
    AVMEDIA_TYPE_VIDEO,
    AVMEDIA_TYPE_AUDIO,
    AVMEDIA_TYPE_DATA,
    AVMEDIA_TYPE_SUBTITLE,
    AVMEDIA_TYPE_ATTACHMENT,
    AVMEDIA_TYPE_NB
};





const char *av_get_media_type_string(enum AVMediaType media_type);
# 277 "./libavutil/avutil.h"
enum AVPictureType {
    AV_PICTURE_TYPE_NONE = 0,
    AV_PICTURE_TYPE_I,
    AV_PICTURE_TYPE_P,
    AV_PICTURE_TYPE_B,
    AV_PICTURE_TYPE_S,
    AV_PICTURE_TYPE_SI,
    AV_PICTURE_TYPE_SP,
    AV_PICTURE_TYPE_BI,
};
# 295 "./libavutil/avutil.h"
char av_get_picture_type_char(enum AVPictureType pict_type);






# 1 "./libavutil/rational.h" 1
# 58 "./libavutil/rational.h"
typedef struct AVRational{
    int num;
    int den;
} AVRational;
# 71 "./libavutil/rational.h"
static inline AVRational av_make_q(int num, int den)
{
    AVRational r = { num, den };
    return r;
}
# 89 "./libavutil/rational.h"
static inline int av_cmp_q(AVRational a, AVRational b){
    const int64_t tmp= a.num * (int64_t)b.den - b.num * (int64_t)a.den;

    if(tmp) return (int)((tmp ^ a.den ^ b.den)>>63)|1;
    else if(b.den && a.den) return 0;
    else if(a.num && b.num) return (a.num>>31) - (b.num>>31);
    else return (-2147483647 -1);
}







static inline double av_q2d(AVRational a){
    return a.num / (double) a.den;
}
# 120 "./libavutil/rational.h"
int av_reduce(int *dst_num, int *dst_den, int64_t num, int64_t den, int64_t max);







AVRational av_mul_q(AVRational b, AVRational c) __attribute__((const));







AVRational av_div_q(AVRational b, AVRational c) __attribute__((const));







AVRational av_add_q(AVRational b, AVRational c) __attribute__((const));







AVRational av_sub_q(AVRational b, AVRational c) __attribute__((const));






static __attribute__((always_inline)) inline AVRational av_inv_q(AVRational q)
{
    AVRational r = { q.den, q.num };
    return r;
}
# 176 "./libavutil/rational.h"
AVRational av_d2q(double d, int max) __attribute__((const));
# 189 "./libavutil/rational.h"
int av_nearer_q(AVRational q, AVRational q1, AVRational q2);
# 198 "./libavutil/rational.h"
int av_find_nearest_q_idx(AVRational q, const AVRational* q_list);
# 209 "./libavutil/rational.h"
uint32_t av_q2intfloat(AVRational q);





AVRational av_gcd_q(AVRational a, AVRational b, int max_den, AVRational def);
# 303 "./libavutil/avutil.h" 2


# 1 "./libavutil/mathematics.h" 1
# 34 "./libavutil/mathematics.h"
# 1 "./libavutil/intfloat.h" 1
# 27 "./libavutil/intfloat.h"
union av_intfloat32 {
    uint32_t i;
    float f;
};

union av_intfloat64 {
    uint64_t i;
    double f;
};




static __attribute__((always_inline)) inline float av_int2float(uint32_t i)
{
    union av_intfloat32 v;
    v.i = i;
    return v.f;
}




static __attribute__((always_inline)) inline uint32_t av_float2int(float f)
{
    union av_intfloat32 v;
    v.f = f;
    return v.i;
}




static __attribute__((always_inline)) inline double av_int2double(uint64_t i)
{
    union av_intfloat64 v;
    v.i = i;
    return v.f;
}




static __attribute__((always_inline)) inline uint64_t av_double2int(double f)
{
    union av_intfloat64 v;
    v.f = f;
    return v.i;
}
# 35 "./libavutil/mathematics.h" 2
# 130 "./libavutil/mathematics.h"
enum AVRounding {
    AV_ROUND_ZERO = 0,
    AV_ROUND_INF = 1,
    AV_ROUND_DOWN = 2,
    AV_ROUND_UP = 3,
    AV_ROUND_NEAR_INF = 5,
# 159 "./libavutil/mathematics.h"
    AV_ROUND_PASS_MINMAX = 8192,
};
# 170 "./libavutil/mathematics.h"
int64_t __attribute__((const)) av_gcd(int64_t a, int64_t b);
# 182 "./libavutil/mathematics.h"
int64_t av_rescale(int64_t a, int64_t b, int64_t c) __attribute__((const));
# 193 "./libavutil/mathematics.h"
int64_t av_rescale_rnd(int64_t a, int64_t b, int64_t c, enum AVRounding rnd) __attribute__((const));
# 204 "./libavutil/mathematics.h"
int64_t av_rescale_q(int64_t a, AVRational bq, AVRational cq) __attribute__((const));
# 213 "./libavutil/mathematics.h"
int64_t av_rescale_q_rnd(int64_t a, AVRational bq, AVRational cq,
                         enum AVRounding rnd) __attribute__((const));
# 228 "./libavutil/mathematics.h"
int av_compare_ts(int64_t ts_a, AVRational tb_a, int64_t ts_b, AVRational tb_b);
# 249 "./libavutil/mathematics.h"
int64_t av_compare_mod(uint64_t a, uint64_t b, uint64_t mod);
# 276 "./libavutil/mathematics.h"
int64_t av_rescale_delta(AVRational in_tb, int64_t in_ts, AVRational fs_tb, int duration, int64_t *last, AVRational out_tb);
# 289 "./libavutil/mathematics.h"
int64_t av_add_stable(AVRational ts_tb, int64_t ts, AVRational inc_tb, int64_t inc);




double av_bessel_i0(double x);
# 306 "./libavutil/avutil.h" 2
# 1 "./libavutil/log.h" 1
# 24 "./libavutil/log.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stdarg.h" 1 3
# 14 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stdarg.h" 3
typedef __builtin_va_list va_list;
# 34 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stdarg.h" 3
typedef __builtin_va_list __gnuc_va_list;
# 25 "./libavutil/log.h" 2



typedef enum {
    AV_CLASS_CATEGORY_NA = 0,
    AV_CLASS_CATEGORY_INPUT,
    AV_CLASS_CATEGORY_OUTPUT,
    AV_CLASS_CATEGORY_MUXER,
    AV_CLASS_CATEGORY_DEMUXER,
    AV_CLASS_CATEGORY_ENCODER,
    AV_CLASS_CATEGORY_DECODER,
    AV_CLASS_CATEGORY_FILTER,
    AV_CLASS_CATEGORY_BITSTREAM_FILTER,
    AV_CLASS_CATEGORY_SWSCALER,
    AV_CLASS_CATEGORY_SWRESAMPLER,
    AV_CLASS_CATEGORY_DEVICE_VIDEO_OUTPUT = 40,
    AV_CLASS_CATEGORY_DEVICE_VIDEO_INPUT,
    AV_CLASS_CATEGORY_DEVICE_AUDIO_OUTPUT,
    AV_CLASS_CATEGORY_DEVICE_AUDIO_INPUT,
    AV_CLASS_CATEGORY_DEVICE_OUTPUT,
    AV_CLASS_CATEGORY_DEVICE_INPUT,
    AV_CLASS_CATEGORY_NB
}AVClassCategory;
# 59 "./libavutil/log.h"
struct AVOptionRanges;






typedef struct AVClass {




    const char* class_name;





    const char* (*item_name)(void* ctx);






    const struct AVOption *option;







    int version;





    int log_level_offset_offset;
# 107 "./libavutil/log.h"
    int parent_log_context_offset;






    AVClassCategory category;





    AVClassCategory (*get_category)(void* ctx);





    int (*query_ranges)(struct AVOptionRanges **, void *obj, const char *key, int flags);




    void* (*child_next)(void *obj, void *prev);
# 146 "./libavutil/log.h"
    const struct AVClass* (*child_class_iterate)(void **iter);
} AVClass;
# 238 "./libavutil/log.h"
void av_log(void *avcl, int level, const char *fmt, ...) __attribute__((__format__(__printf__, 3, 4)));
# 259 "./libavutil/log.h"
void av_log_once(void* avcl, int initial_level, int subsequent_level, int *state, const char *fmt, ...) __attribute__((__format__(__printf__, 5, 6)));
# 277 "./libavutil/log.h"
void av_vlog(void *avcl, int level, const char *fmt, va_list vl);
# 286 "./libavutil/log.h"
int av_log_get_level(void);
# 295 "./libavutil/log.h"
void av_log_set_level(int level);
# 307 "./libavutil/log.h"
void av_log_set_callback(void (*callback)(void*, int, const char*, va_list));
# 322 "./libavutil/log.h"
void av_log_default_callback(void *avcl, int level, const char *fmt,
                             va_list vl);
# 332 "./libavutil/log.h"
const char* av_default_item_name(void* ctx);
AVClassCategory av_default_get_category(void *ptr);
# 342 "./libavutil/log.h"
void av_log_format_line(void *ptr, int level, const char *fmt, va_list vl,
                        char *line, int line_size, int *print_prefix);
# 359 "./libavutil/log.h"
int av_log_format_line2(void *ptr, int level, const char *fmt, va_list vl,
                        char *line, int line_size, int *print_prefix);
# 380 "./libavutil/log.h"
void av_log_set_flags(int arg);
int av_log_get_flags(void);
# 307 "./libavutil/avutil.h" 2
# 1 "./libavutil/pixfmt.h" 1
# 64 "./libavutil/pixfmt.h"
enum AVPixelFormat {
    AV_PIX_FMT_NONE = -1,
    AV_PIX_FMT_YUV420P,
    AV_PIX_FMT_YUYV422,
    AV_PIX_FMT_RGB24,
    AV_PIX_FMT_BGR24,
    AV_PIX_FMT_YUV422P,
    AV_PIX_FMT_YUV444P,
    AV_PIX_FMT_YUV410P,
    AV_PIX_FMT_YUV411P,
    AV_PIX_FMT_GRAY8,
    AV_PIX_FMT_MONOWHITE,
    AV_PIX_FMT_MONOBLACK,
    AV_PIX_FMT_PAL8,
    AV_PIX_FMT_YUVJ420P,
    AV_PIX_FMT_YUVJ422P,
    AV_PIX_FMT_YUVJ444P,
    AV_PIX_FMT_UYVY422,
    AV_PIX_FMT_UYYVYY411,
    AV_PIX_FMT_BGR8,
    AV_PIX_FMT_BGR4,
    AV_PIX_FMT_BGR4_BYTE,
    AV_PIX_FMT_RGB8,
    AV_PIX_FMT_RGB4,
    AV_PIX_FMT_RGB4_BYTE,
    AV_PIX_FMT_NV12,
    AV_PIX_FMT_NV21,

    AV_PIX_FMT_ARGB,
    AV_PIX_FMT_RGBA,
    AV_PIX_FMT_ABGR,
    AV_PIX_FMT_BGRA,

    AV_PIX_FMT_GRAY16BE,
    AV_PIX_FMT_GRAY16LE,
    AV_PIX_FMT_YUV440P,
    AV_PIX_FMT_YUVJ440P,
    AV_PIX_FMT_YUVA420P,
    AV_PIX_FMT_RGB48BE,
    AV_PIX_FMT_RGB48LE,

    AV_PIX_FMT_RGB565BE,
    AV_PIX_FMT_RGB565LE,
    AV_PIX_FMT_RGB555BE,
    AV_PIX_FMT_RGB555LE,

    AV_PIX_FMT_BGR565BE,
    AV_PIX_FMT_BGR565LE,
    AV_PIX_FMT_BGR555BE,
    AV_PIX_FMT_BGR555LE,





    AV_PIX_FMT_VAAPI,

    AV_PIX_FMT_YUV420P16LE,
    AV_PIX_FMT_YUV420P16BE,
    AV_PIX_FMT_YUV422P16LE,
    AV_PIX_FMT_YUV422P16BE,
    AV_PIX_FMT_YUV444P16LE,
    AV_PIX_FMT_YUV444P16BE,
    AV_PIX_FMT_DXVA2_VLD,

    AV_PIX_FMT_RGB444LE,
    AV_PIX_FMT_RGB444BE,
    AV_PIX_FMT_BGR444LE,
    AV_PIX_FMT_BGR444BE,
    AV_PIX_FMT_YA8,

    AV_PIX_FMT_Y400A = AV_PIX_FMT_YA8,
    AV_PIX_FMT_GRAY8A= AV_PIX_FMT_YA8,

    AV_PIX_FMT_BGR48BE,
    AV_PIX_FMT_BGR48LE,






    AV_PIX_FMT_YUV420P9BE,
    AV_PIX_FMT_YUV420P9LE,
    AV_PIX_FMT_YUV420P10BE,
    AV_PIX_FMT_YUV420P10LE,
    AV_PIX_FMT_YUV422P10BE,
    AV_PIX_FMT_YUV422P10LE,
    AV_PIX_FMT_YUV444P9BE,
    AV_PIX_FMT_YUV444P9LE,
    AV_PIX_FMT_YUV444P10BE,
    AV_PIX_FMT_YUV444P10LE,
    AV_PIX_FMT_YUV422P9BE,
    AV_PIX_FMT_YUV422P9LE,
    AV_PIX_FMT_GBRP,
    AV_PIX_FMT_GBR24P = AV_PIX_FMT_GBRP,
    AV_PIX_FMT_GBRP9BE,
    AV_PIX_FMT_GBRP9LE,
    AV_PIX_FMT_GBRP10BE,
    AV_PIX_FMT_GBRP10LE,
    AV_PIX_FMT_GBRP16BE,
    AV_PIX_FMT_GBRP16LE,
    AV_PIX_FMT_YUVA422P,
    AV_PIX_FMT_YUVA444P,
    AV_PIX_FMT_YUVA420P9BE,
    AV_PIX_FMT_YUVA420P9LE,
    AV_PIX_FMT_YUVA422P9BE,
    AV_PIX_FMT_YUVA422P9LE,
    AV_PIX_FMT_YUVA444P9BE,
    AV_PIX_FMT_YUVA444P9LE,
    AV_PIX_FMT_YUVA420P10BE,
    AV_PIX_FMT_YUVA420P10LE,
    AV_PIX_FMT_YUVA422P10BE,
    AV_PIX_FMT_YUVA422P10LE,
    AV_PIX_FMT_YUVA444P10BE,
    AV_PIX_FMT_YUVA444P10LE,
    AV_PIX_FMT_YUVA420P16BE,
    AV_PIX_FMT_YUVA420P16LE,
    AV_PIX_FMT_YUVA422P16BE,
    AV_PIX_FMT_YUVA422P16LE,
    AV_PIX_FMT_YUVA444P16BE,
    AV_PIX_FMT_YUVA444P16LE,

    AV_PIX_FMT_VDPAU,

    AV_PIX_FMT_XYZ12LE,
    AV_PIX_FMT_XYZ12BE,
    AV_PIX_FMT_NV16,
    AV_PIX_FMT_NV20LE,
    AV_PIX_FMT_NV20BE,

    AV_PIX_FMT_RGBA64BE,
    AV_PIX_FMT_RGBA64LE,
    AV_PIX_FMT_BGRA64BE,
    AV_PIX_FMT_BGRA64LE,

    AV_PIX_FMT_YVYU422,

    AV_PIX_FMT_YA16BE,
    AV_PIX_FMT_YA16LE,

    AV_PIX_FMT_GBRAP,
    AV_PIX_FMT_GBRAP16BE,
    AV_PIX_FMT_GBRAP16LE,
# 240 "./libavutil/pixfmt.h"
    AV_PIX_FMT_QSV,




    AV_PIX_FMT_MMAL,

    AV_PIX_FMT_D3D11VA_VLD,





    AV_PIX_FMT_CUDA,

    AV_PIX_FMT_0RGB,
    AV_PIX_FMT_RGB0,
    AV_PIX_FMT_0BGR,
    AV_PIX_FMT_BGR0,

    AV_PIX_FMT_YUV420P12BE,
    AV_PIX_FMT_YUV420P12LE,
    AV_PIX_FMT_YUV420P14BE,
    AV_PIX_FMT_YUV420P14LE,
    AV_PIX_FMT_YUV422P12BE,
    AV_PIX_FMT_YUV422P12LE,
    AV_PIX_FMT_YUV422P14BE,
    AV_PIX_FMT_YUV422P14LE,
    AV_PIX_FMT_YUV444P12BE,
    AV_PIX_FMT_YUV444P12LE,
    AV_PIX_FMT_YUV444P14BE,
    AV_PIX_FMT_YUV444P14LE,
    AV_PIX_FMT_GBRP12BE,
    AV_PIX_FMT_GBRP12LE,
    AV_PIX_FMT_GBRP14BE,
    AV_PIX_FMT_GBRP14LE,
    AV_PIX_FMT_YUVJ411P,

    AV_PIX_FMT_BAYER_BGGR8,
    AV_PIX_FMT_BAYER_RGGB8,
    AV_PIX_FMT_BAYER_GBRG8,
    AV_PIX_FMT_BAYER_GRBG8,
    AV_PIX_FMT_BAYER_BGGR16LE,
    AV_PIX_FMT_BAYER_BGGR16BE,
    AV_PIX_FMT_BAYER_RGGB16LE,
    AV_PIX_FMT_BAYER_RGGB16BE,
    AV_PIX_FMT_BAYER_GBRG16LE,
    AV_PIX_FMT_BAYER_GBRG16BE,
    AV_PIX_FMT_BAYER_GRBG16LE,
    AV_PIX_FMT_BAYER_GRBG16BE,


    AV_PIX_FMT_XVMC,


    AV_PIX_FMT_YUV440P10LE,
    AV_PIX_FMT_YUV440P10BE,
    AV_PIX_FMT_YUV440P12LE,
    AV_PIX_FMT_YUV440P12BE,
    AV_PIX_FMT_AYUV64LE,
    AV_PIX_FMT_AYUV64BE,

    AV_PIX_FMT_VIDEOTOOLBOX,

    AV_PIX_FMT_P010LE,
    AV_PIX_FMT_P010BE,

    AV_PIX_FMT_GBRAP12BE,
    AV_PIX_FMT_GBRAP12LE,

    AV_PIX_FMT_GBRAP10BE,
    AV_PIX_FMT_GBRAP10LE,

    AV_PIX_FMT_MEDIACODEC,

    AV_PIX_FMT_GRAY12BE,
    AV_PIX_FMT_GRAY12LE,
    AV_PIX_FMT_GRAY10BE,
    AV_PIX_FMT_GRAY10LE,

    AV_PIX_FMT_P016LE,
    AV_PIX_FMT_P016BE,
# 333 "./libavutil/pixfmt.h"
    AV_PIX_FMT_D3D11,

    AV_PIX_FMT_GRAY9BE,
    AV_PIX_FMT_GRAY9LE,

    AV_PIX_FMT_GBRPF32BE,
    AV_PIX_FMT_GBRPF32LE,
    AV_PIX_FMT_GBRAPF32BE,
    AV_PIX_FMT_GBRAPF32LE,






    AV_PIX_FMT_DRM_PRIME,






    AV_PIX_FMT_OPENCL,

    AV_PIX_FMT_GRAY14BE,
    AV_PIX_FMT_GRAY14LE,

    AV_PIX_FMT_GRAYF32BE,
    AV_PIX_FMT_GRAYF32LE,

    AV_PIX_FMT_YUVA422P12BE,
    AV_PIX_FMT_YUVA422P12LE,
    AV_PIX_FMT_YUVA444P12BE,
    AV_PIX_FMT_YUVA444P12LE,

    AV_PIX_FMT_NV24,
    AV_PIX_FMT_NV42,






    AV_PIX_FMT_VULKAN,

    AV_PIX_FMT_Y210BE,
    AV_PIX_FMT_Y210LE,

    AV_PIX_FMT_X2RGB10LE,
    AV_PIX_FMT_X2RGB10BE,
    AV_PIX_FMT_X2BGR10LE,
    AV_PIX_FMT_X2BGR10BE,

    AV_PIX_FMT_P210BE,
    AV_PIX_FMT_P210LE,

    AV_PIX_FMT_P410BE,
    AV_PIX_FMT_P410LE,

    AV_PIX_FMT_P216BE,
    AV_PIX_FMT_P216LE,

    AV_PIX_FMT_P416BE,
    AV_PIX_FMT_P416LE,

    AV_PIX_FMT_VUYA,

    AV_PIX_FMT_RGBAF16BE,
    AV_PIX_FMT_RGBAF16LE,

    AV_PIX_FMT_VUYX,

    AV_PIX_FMT_P012LE,
    AV_PIX_FMT_P012BE,

    AV_PIX_FMT_Y212BE,
    AV_PIX_FMT_Y212LE,

    AV_PIX_FMT_XV30BE,
    AV_PIX_FMT_XV30LE,

    AV_PIX_FMT_XV36BE,
    AV_PIX_FMT_XV36LE,

    AV_PIX_FMT_RGBF32BE,
    AV_PIX_FMT_RGBF32LE,

    AV_PIX_FMT_RGBAF32BE,
    AV_PIX_FMT_RGBAF32LE,

    AV_PIX_FMT_P212BE,
    AV_PIX_FMT_P212LE,

    AV_PIX_FMT_P412BE,
    AV_PIX_FMT_P412LE,

    AV_PIX_FMT_GBRAP14BE,
    AV_PIX_FMT_GBRAP14LE,






    AV_PIX_FMT_D3D12,

    AV_PIX_FMT_NB
};
# 552 "./libavutil/pixfmt.h"
enum AVColorPrimaries {
    AVCOL_PRI_RESERVED0 = 0,
    AVCOL_PRI_BT709 = 1,
    AVCOL_PRI_UNSPECIFIED = 2,
    AVCOL_PRI_RESERVED = 3,
    AVCOL_PRI_BT470M = 4,

    AVCOL_PRI_BT470BG = 5,
    AVCOL_PRI_SMPTE170M = 6,
    AVCOL_PRI_SMPTE240M = 7,
    AVCOL_PRI_FILM = 8,
    AVCOL_PRI_BT2020 = 9,
    AVCOL_PRI_SMPTE428 = 10,
    AVCOL_PRI_SMPTEST428_1 = AVCOL_PRI_SMPTE428,
    AVCOL_PRI_SMPTE431 = 11,
    AVCOL_PRI_SMPTE432 = 12,
    AVCOL_PRI_EBU3213 = 22,
    AVCOL_PRI_JEDEC_P22 = AVCOL_PRI_EBU3213,
    AVCOL_PRI_NB
};





enum AVColorTransferCharacteristic {
    AVCOL_TRC_RESERVED0 = 0,
    AVCOL_TRC_BT709 = 1,
    AVCOL_TRC_UNSPECIFIED = 2,
    AVCOL_TRC_RESERVED = 3,
    AVCOL_TRC_GAMMA22 = 4,
    AVCOL_TRC_GAMMA28 = 5,
    AVCOL_TRC_SMPTE170M = 6,
    AVCOL_TRC_SMPTE240M = 7,
    AVCOL_TRC_LINEAR = 8,
    AVCOL_TRC_LOG = 9,
    AVCOL_TRC_LOG_SQRT = 10,
    AVCOL_TRC_IEC61966_2_4 = 11,
    AVCOL_TRC_BT1361_ECG = 12,
    AVCOL_TRC_IEC61966_2_1 = 13,
    AVCOL_TRC_BT2020_10 = 14,
    AVCOL_TRC_BT2020_12 = 15,
    AVCOL_TRC_SMPTE2084 = 16,
    AVCOL_TRC_SMPTEST2084 = AVCOL_TRC_SMPTE2084,
    AVCOL_TRC_SMPTE428 = 17,
    AVCOL_TRC_SMPTEST428_1 = AVCOL_TRC_SMPTE428,
    AVCOL_TRC_ARIB_STD_B67 = 18,
    AVCOL_TRC_NB
};





enum AVColorSpace {
    AVCOL_SPC_RGB = 0,
    AVCOL_SPC_BT709 = 1,
    AVCOL_SPC_UNSPECIFIED = 2,
    AVCOL_SPC_RESERVED = 3,
    AVCOL_SPC_FCC = 4,
    AVCOL_SPC_BT470BG = 5,
    AVCOL_SPC_SMPTE170M = 6,
    AVCOL_SPC_SMPTE240M = 7,
    AVCOL_SPC_YCGCO = 8,
    AVCOL_SPC_YCOCG = AVCOL_SPC_YCGCO,
    AVCOL_SPC_BT2020_NCL = 9,
    AVCOL_SPC_BT2020_CL = 10,
    AVCOL_SPC_SMPTE2085 = 11,
    AVCOL_SPC_CHROMA_DERIVED_NCL = 12,
    AVCOL_SPC_CHROMA_DERIVED_CL = 13,
    AVCOL_SPC_ICTCP = 14,
    AVCOL_SPC_NB
};
# 645 "./libavutil/pixfmt.h"
enum AVColorRange {
    AVCOL_RANGE_UNSPECIFIED = 0,
# 663 "./libavutil/pixfmt.h"
    AVCOL_RANGE_MPEG = 1,
# 680 "./libavutil/pixfmt.h"
    AVCOL_RANGE_JPEG = 2,
    AVCOL_RANGE_NB
};
# 699 "./libavutil/pixfmt.h"
enum AVChromaLocation {
    AVCHROMA_LOC_UNSPECIFIED = 0,
    AVCHROMA_LOC_LEFT = 1,
    AVCHROMA_LOC_CENTER = 2,
    AVCHROMA_LOC_TOPLEFT = 3,
    AVCHROMA_LOC_TOP = 4,
    AVCHROMA_LOC_BOTTOMLEFT = 5,
    AVCHROMA_LOC_BOTTOM = 6,
    AVCHROMA_LOC_NB
};
# 308 "./libavutil/avutil.h" 2




static inline void *av_x_if_null(const void *p, const void *x)
{
    return (void *)(intptr_t)(p ? p : x);
}
# 325 "./libavutil/avutil.h"
unsigned av_int_list_length_for_size(unsigned elsize,
                                     const void *list, uint64_t term) __attribute__((pure));
# 347 "./libavutil/avutil.h"
__attribute__((deprecated))
FILE *av_fopen_utf8(const char *path, const char *mode);





AVRational av_get_time_base_q(void);
# 368 "./libavutil/avutil.h"
char *av_fourcc_make_string(char *buf, uint32_t fourcc);
# 32 "./libavutil/frame.h" 2
# 1 "./libavutil/buffer.h" 1
# 28 "./libavutil/buffer.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 29 "./libavutil/buffer.h" 2
# 74 "./libavutil/buffer.h"
typedef struct AVBuffer AVBuffer;







typedef struct AVBufferRef {
    AVBuffer *buffer;






    uint8_t *data;



    size_t size;
} AVBufferRef;






AVBufferRef *av_buffer_alloc(size_t size);





AVBufferRef *av_buffer_allocz(size_t size);
# 131 "./libavutil/buffer.h"
AVBufferRef *av_buffer_create(uint8_t *data, size_t size,
                              void (*free)(void *opaque, uint8_t *data),
                              void *opaque, int flags);






void av_buffer_default_free(void *opaque, uint8_t *data);







AVBufferRef *av_buffer_ref(const AVBufferRef *buf);







void av_buffer_unref(AVBufferRef **buf);







int av_buffer_is_writable(const AVBufferRef *buf);




void *av_buffer_get_opaque(const AVBufferRef *buf);

int av_buffer_get_ref_count(const AVBufferRef *buf);
# 182 "./libavutil/buffer.h"
int av_buffer_make_writable(AVBufferRef **buf);
# 199 "./libavutil/buffer.h"
int av_buffer_realloc(AVBufferRef **buf, size_t size);
# 215 "./libavutil/buffer.h"
int av_buffer_replace(AVBufferRef **dst, const AVBufferRef *src);
# 255 "./libavutil/buffer.h"
typedef struct AVBufferPool AVBufferPool;
# 266 "./libavutil/buffer.h"
AVBufferPool *av_buffer_pool_init(size_t size, AVBufferRef* (*alloc)(size_t size));
# 283 "./libavutil/buffer.h"
AVBufferPool *av_buffer_pool_init2(size_t size, void *opaque,
                                   AVBufferRef* (*alloc)(void *opaque, size_t size),
                                   void (*pool_free)(void *opaque));
# 295 "./libavutil/buffer.h"
void av_buffer_pool_uninit(AVBufferPool **pool);







AVBufferRef *av_buffer_pool_get(AVBufferPool *pool);
# 316 "./libavutil/buffer.h"
void *av_buffer_pool_buffer_get_opaque(const AVBufferRef *ref);
# 33 "./libavutil/frame.h" 2

# 1 "./libavutil/dict.h" 1
# 89 "./libavutil/dict.h"
typedef struct AVDictionaryEntry {
    char *key;
    char *value;
} AVDictionaryEntry;

typedef struct AVDictionary AVDictionary;
# 110 "./libavutil/dict.h"
AVDictionaryEntry *av_dict_get(const AVDictionary *m, const char *key,
                               const AVDictionaryEntry *prev, int flags);
# 137 "./libavutil/dict.h"
const AVDictionaryEntry *av_dict_iterate(const AVDictionary *m,
                                         const AVDictionaryEntry *prev);







int av_dict_count(const AVDictionary *m);
# 165 "./libavutil/dict.h"
int av_dict_set(AVDictionary **pm, const char *key, const char *value, int flags);







int av_dict_set_int(AVDictionary **pm, const char *key, int64_t value, int flags);
# 192 "./libavutil/dict.h"
int av_dict_parse_string(AVDictionary **pm, const char *str,
                         const char *key_val_sep, const char *pairs_sep,
                         int flags);
# 209 "./libavutil/dict.h"
int av_dict_copy(AVDictionary **dst, const AVDictionary *src, int flags);





void av_dict_free(AVDictionary **m);
# 234 "./libavutil/dict.h"
int av_dict_get_string(const AVDictionary *m, char **buffer,
                       const char key_val_sep, const char pairs_sep);
# 35 "./libavutil/frame.h" 2

# 1 "./libavutil/samplefmt.h" 1
# 55 "./libavutil/samplefmt.h"
enum AVSampleFormat {
    AV_SAMPLE_FMT_NONE = -1,
    AV_SAMPLE_FMT_U8,
    AV_SAMPLE_FMT_S16,
    AV_SAMPLE_FMT_S32,
    AV_SAMPLE_FMT_FLT,
    AV_SAMPLE_FMT_DBL,

    AV_SAMPLE_FMT_U8P,
    AV_SAMPLE_FMT_S16P,
    AV_SAMPLE_FMT_S32P,
    AV_SAMPLE_FMT_FLTP,
    AV_SAMPLE_FMT_DBLP,
    AV_SAMPLE_FMT_S64,
    AV_SAMPLE_FMT_S64P,

    AV_SAMPLE_FMT_NB
};





const char *av_get_sample_fmt_name(enum AVSampleFormat sample_fmt);





enum AVSampleFormat av_get_sample_fmt(const char *name);







enum AVSampleFormat av_get_alt_sample_fmt(enum AVSampleFormat sample_fmt, int planar);
# 103 "./libavutil/samplefmt.h"
enum AVSampleFormat av_get_packed_sample_fmt(enum AVSampleFormat sample_fmt);
# 114 "./libavutil/samplefmt.h"
enum AVSampleFormat av_get_planar_sample_fmt(enum AVSampleFormat sample_fmt);
# 128 "./libavutil/samplefmt.h"
char *av_get_sample_fmt_string(char *buf, int buf_size, enum AVSampleFormat sample_fmt);
# 137 "./libavutil/samplefmt.h"
int av_get_bytes_per_sample(enum AVSampleFormat sample_fmt);







int av_sample_fmt_is_planar(enum AVSampleFormat sample_fmt);
# 157 "./libavutil/samplefmt.h"
int av_samples_get_buffer_size(int *linesize, int nb_channels, int nb_samples,
                               enum AVSampleFormat sample_fmt, int align);
# 198 "./libavutil/samplefmt.h"
int av_samples_fill_arrays(uint8_t **audio_data, int *linesize,
                           const uint8_t *buf,
                           int nb_channels, int nb_samples,
                           enum AVSampleFormat sample_fmt, int align);
# 223 "./libavutil/samplefmt.h"
int av_samples_alloc(uint8_t **audio_data, int *linesize, int nb_channels,
                     int nb_samples, enum AVSampleFormat sample_fmt, int align);
# 235 "./libavutil/samplefmt.h"
int av_samples_alloc_array_and_samples(uint8_t ***audio_data, int *linesize, int nb_channels,
                                       int nb_samples, enum AVSampleFormat sample_fmt, int align);
# 249 "./libavutil/samplefmt.h"
int av_samples_copy(uint8_t * const *dst, uint8_t * const *src, int dst_offset,
                    int src_offset, int nb_samples, int nb_channels,
                    enum AVSampleFormat sample_fmt);
# 262 "./libavutil/samplefmt.h"
int av_samples_set_silence(uint8_t * const *audio_data, int offset, int nb_samples,
                           int nb_channels, enum AVSampleFormat sample_fmt);
# 37 "./libavutil/frame.h" 2
# 49 "./libavutil/frame.h"
enum AVFrameSideDataType {



    AV_FRAME_DATA_PANSCAN,





    AV_FRAME_DATA_A53_CC,




    AV_FRAME_DATA_STEREO3D,



    AV_FRAME_DATA_MATRIXENCODING,




    AV_FRAME_DATA_DOWNMIX_INFO,



    AV_FRAME_DATA_REPLAYGAIN,







    AV_FRAME_DATA_DISPLAYMATRIX,




    AV_FRAME_DATA_AFD,






    AV_FRAME_DATA_MOTION_VECTORS,
# 109 "./libavutil/frame.h"
    AV_FRAME_DATA_SKIP_SAMPLES,




    AV_FRAME_DATA_AUDIO_SERVICE_TYPE,





    AV_FRAME_DATA_MASTERING_DISPLAY_METADATA,




    AV_FRAME_DATA_GOP_TIMECODE,





    AV_FRAME_DATA_SPHERICAL,





    AV_FRAME_DATA_CONTENT_LIGHT_LEVEL,






    AV_FRAME_DATA_ICC_PROFILE,







    AV_FRAME_DATA_S12M_TIMECODE,






    AV_FRAME_DATA_DYNAMIC_HDR_PLUS,





    AV_FRAME_DATA_REGIONS_OF_INTEREST,




    AV_FRAME_DATA_VIDEO_ENC_PARAMS,







    AV_FRAME_DATA_SEI_UNREGISTERED,





    AV_FRAME_DATA_FILM_GRAIN_PARAMS,





    AV_FRAME_DATA_DETECTION_BBOXES,






    AV_FRAME_DATA_DOVI_RPU_BUFFER,






    AV_FRAME_DATA_DOVI_METADATA,






    AV_FRAME_DATA_DYNAMIC_HDR_VIVID,




    AV_FRAME_DATA_AMBIENT_VIEWING_ENVIRONMENT,
# 226 "./libavutil/frame.h"
    AV_FRAME_DATA_VIDEO_HINT,
};

enum AVActiveFormatDescription {
    AV_AFD_SAME = 8,
    AV_AFD_4_3 = 9,
    AV_AFD_16_9 = 10,
    AV_AFD_14_9 = 11,
    AV_AFD_4_3_SP_14_9 = 13,
    AV_AFD_16_9_SP_14_9 = 14,
    AV_AFD_SP_4_3 = 15,
};
# 246 "./libavutil/frame.h"
typedef struct AVFrameSideData {
    enum AVFrameSideDataType type;
    uint8_t *data;
    size_t size;
    AVDictionary *metadata;
    AVBufferRef *buf;
} AVFrameSideData;
# 265 "./libavutil/frame.h"
typedef struct AVRegionOfInterest {




    uint32_t self_size;
# 280 "./libavutil/frame.h"
    int top;
    int bottom;
    int left;
    int right;
# 307 "./libavutil/frame.h"
    AVRational qoffset;
} AVRegionOfInterest;
# 340 "./libavutil/frame.h"
typedef struct AVFrame {
# 361 "./libavutil/frame.h"
    uint8_t *data[8];
# 385 "./libavutil/frame.h"
    int linesize[8];
# 401 "./libavutil/frame.h"
    uint8_t **extended_data;
# 412 "./libavutil/frame.h"
    int width, height;







    int nb_samples;






    int format;







    __attribute__((deprecated))
    int key_frame;





    enum AVPictureType pict_type;




    AVRational sample_aspect_ratio;




    int64_t pts;






    int64_t pkt_dts;







    AVRational time_base;





    __attribute__((deprecated))
    int coded_picture_number;



    __attribute__((deprecated))
    int display_picture_number;





    int quality;
# 501 "./libavutil/frame.h"
    void *opaque;
# 521 "./libavutil/frame.h"
    int repeat_pict;







    __attribute__((deprecated))
    int interlaced_frame;






    __attribute__((deprecated))
    int top_field_first;






    __attribute__((deprecated))
    int palette_has_changed;
# 560 "./libavutil/frame.h"
    __attribute__((deprecated))
    int64_t reordered_opaque;





    int sample_rate;






    __attribute__((deprecated))
    uint64_t channel_layout;
# 590 "./libavutil/frame.h"
    AVBufferRef *buf[8];
# 604 "./libavutil/frame.h"
    AVBufferRef **extended_buf;



    int nb_extended_buf;

    AVFrameSideData **side_data;
    int nb_side_data;
# 649 "./libavutil/frame.h"
    int flags;






    enum AVColorRange color_range;

    enum AVColorPrimaries color_primaries;

    enum AVColorTransferCharacteristic color_trc;






    enum AVColorSpace colorspace;

    enum AVChromaLocation chroma_location;






    int64_t best_effort_timestamp;
# 686 "./libavutil/frame.h"
    __attribute__((deprecated))
    int64_t pkt_pos;
# 699 "./libavutil/frame.h"
    __attribute__((deprecated))
    int64_t pkt_duration;







    AVDictionary *metadata;
# 717 "./libavutil/frame.h"
    int decode_error_flags;
# 730 "./libavutil/frame.h"
    __attribute__((deprecated))
    int channels;
# 744 "./libavutil/frame.h"
    __attribute__((deprecated))
    int pkt_size;






    AVBufferRef *hw_frames_ctx;
# 768 "./libavutil/frame.h"
    AVBufferRef *opaque_ref;
# 778 "./libavutil/frame.h"
    size_t crop_top;
    size_t crop_bottom;
    size_t crop_left;
    size_t crop_right;
# 797 "./libavutil/frame.h"
    AVBufferRef *private_ref;




    AVChannelLayout ch_layout;




    int64_t duration;
} AVFrame;
# 821 "./libavutil/frame.h"
AVFrame *av_frame_alloc(void);
# 830 "./libavutil/frame.h"
void av_frame_free(AVFrame **frame);
# 847 "./libavutil/frame.h"
int av_frame_ref(AVFrame *dst, const AVFrame *src);
# 860 "./libavutil/frame.h"
int av_frame_replace(AVFrame *dst, const AVFrame *src);
# 869 "./libavutil/frame.h"
AVFrame *av_frame_clone(const AVFrame *src);




void av_frame_unref(AVFrame *frame);
# 883 "./libavutil/frame.h"
void av_frame_move_ref(AVFrame *dst, AVFrame *src);
# 908 "./libavutil/frame.h"
int av_frame_get_buffer(AVFrame *frame, int align);
# 922 "./libavutil/frame.h"
int av_frame_is_writable(AVFrame *frame);
# 936 "./libavutil/frame.h"
int av_frame_make_writable(AVFrame *frame);
# 949 "./libavutil/frame.h"
int av_frame_copy(AVFrame *dst, const AVFrame *src);
# 959 "./libavutil/frame.h"
int av_frame_copy_props(AVFrame *dst, const AVFrame *src);
# 970 "./libavutil/frame.h"
AVBufferRef *av_frame_get_plane_buffer(const AVFrame *frame, int plane);
# 981 "./libavutil/frame.h"
AVFrameSideData *av_frame_new_side_data(AVFrame *frame,
                                        enum AVFrameSideDataType type,
                                        size_t size);
# 997 "./libavutil/frame.h"
AVFrameSideData *av_frame_new_side_data_from_buf(AVFrame *frame,
                                                 enum AVFrameSideDataType type,
                                                 AVBufferRef *buf);





AVFrameSideData *av_frame_get_side_data(const AVFrame *frame,
                                        enum AVFrameSideDataType type);




void av_frame_remove_side_data(AVFrame *frame, enum AVFrameSideDataType type);





enum {
# 1026 "./libavutil/frame.h"
    AV_FRAME_CROP_UNALIGNED = 1 << 0,
};
# 1045 "./libavutil/frame.h"
int av_frame_apply_cropping(AVFrame *frame, int flags);




const char *av_frame_side_data_name(enum AVFrameSideDataType type);
# 35 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2
# 1 "./libavutil/intreadwrite.h" 1
# 25 "./libavutil/intreadwrite.h"
# 1 "./libavutil/bswap.h" 1
# 60 "./libavutil/bswap.h"
static __attribute__((always_inline)) inline __attribute__((const)) uint16_t av_bswap16(uint16_t x)
{
    x= (x>>8) | (x<<8);
    return x;
}



static __attribute__((always_inline)) inline __attribute__((const)) uint32_t av_bswap32(uint32_t x)
{
    return ((((x) << 8 & 0xff00) | ((x) >> 8 & 0x00ff)) << 16 | ((((x) >> 16) << 8 & 0xff00) | (((x) >> 16) >> 8 & 0x00ff)));
}



static inline uint64_t __attribute__((const)) av_bswap64(uint64_t x)
{
    return (uint64_t)av_bswap32(x) << 32 | av_bswap32(x >> 32);
}
# 26 "./libavutil/intreadwrite.h" 2

typedef union {
    uint64_t u64;
    uint32_t u32[2];
    uint16_t u16[4];
    uint8_t u8 [8];
    double f64;
    float f32[2];
} __attribute__((may_alias)) av_alias64;

typedef union {
    uint32_t u32;
    uint16_t u16[2];
    uint8_t u8 [4];
    float f32;
} __attribute__((may_alias)) av_alias32;

typedef union {
    uint16_t u16;
    uint8_t u8 [2];
} __attribute__((may_alias)) av_alias16;
# 218 "./libavutil/intreadwrite.h"
union unaligned_64 { uint64_t l; } __attribute__((packed)) __attribute__((may_alias));
union unaligned_32 { uint32_t l; } __attribute__((packed)) __attribute__((may_alias));
union unaligned_16 { uint16_t l; } __attribute__((packed)) __attribute__((may_alias));
# 36 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2

# 1 "./libavutil/opt.h" 1
# 223 "./libavutil/opt.h"
enum AVOptionType{
    AV_OPT_TYPE_FLAGS,
    AV_OPT_TYPE_INT,
    AV_OPT_TYPE_INT64,
    AV_OPT_TYPE_DOUBLE,
    AV_OPT_TYPE_FLOAT,
    AV_OPT_TYPE_STRING,
    AV_OPT_TYPE_RATIONAL,
    AV_OPT_TYPE_BINARY,
    AV_OPT_TYPE_DICT,
    AV_OPT_TYPE_UINT64,
    AV_OPT_TYPE_CONST,
    AV_OPT_TYPE_IMAGE_SIZE,
    AV_OPT_TYPE_PIXEL_FMT,
    AV_OPT_TYPE_SAMPLE_FMT,
    AV_OPT_TYPE_VIDEO_RATE,
    AV_OPT_TYPE_DURATION,
    AV_OPT_TYPE_COLOR,

    AV_OPT_TYPE_CHANNEL_LAYOUT,

    AV_OPT_TYPE_BOOL,
    AV_OPT_TYPE_CHLAYOUT,
};




typedef struct AVOption {
    const char *name;





    const char *help;





    int offset;
    enum AVOptionType type;




    union {
        int64_t i64;
        double dbl;
        const char *str;

        AVRational q;
    } default_val;
    double min;
    double max;

    int flags;
# 307 "./libavutil/opt.h"
    const char *unit;
} AVOption;




typedef struct AVOptionRange {
    const char *str;





    double value_min, value_max;




    double component_min, component_max;




    int is_range;
} AVOptionRange;




typedef struct AVOptionRanges {
# 367 "./libavutil/opt.h"
    AVOptionRange **range;



    int nb_ranges;



    int nb_components;
} AVOptionRanges;
# 387 "./libavutil/opt.h"
int av_opt_show2(void *obj, void *av_log_obj, int req_flags, int rej_flags);






void av_opt_set_defaults(void *s);
# 405 "./libavutil/opt.h"
void av_opt_set_defaults2(void *s, int mask, int flags);
# 424 "./libavutil/opt.h"
int av_set_options_string(void *ctx, const char *opts,
                          const char *key_val_sep, const char *pairs_sep);
# 454 "./libavutil/opt.h"
int av_opt_set_from_string(void *ctx, const char *opts,
                           const char *const *shorthand,
                           const char *key_val_sep, const char *pairs_sep);



void av_opt_free(void *obj);
# 470 "./libavutil/opt.h"
int av_opt_flag_is_set(void *obj, const char *field_name, const char *flag_name);
# 486 "./libavutil/opt.h"
int av_opt_set_dict(void *obj, struct AVDictionary **options);
# 504 "./libavutil/opt.h"
int av_opt_set_dict2(void *obj, struct AVDictionary **options, int search_flags);
# 525 "./libavutil/opt.h"
int av_opt_get_key_value(const char **ropts,
                         const char *key_val_sep, const char *pairs_sep,
                         unsigned flags,
                         char **rkey, char **rval);

enum {





    AV_OPT_FLAG_IMPLICIT_KEY = 1,
};
# 553 "./libavutil/opt.h"
int av_opt_eval_flags (void *obj, const AVOption *o, const char *val, int *flags_out);
int av_opt_eval_int (void *obj, const AVOption *o, const char *val, int *int_out);
int av_opt_eval_int64 (void *obj, const AVOption *o, const char *val, int64_t *int64_out);
int av_opt_eval_float (void *obj, const AVOption *o, const char *val, float *float_out);
int av_opt_eval_double(void *obj, const AVOption *o, const char *val, double *double_out);
int av_opt_eval_q (void *obj, const AVOption *o, const char *val, AVRational *q_out);
# 608 "./libavutil/opt.h"
const AVOption *av_opt_find(void *obj, const char *name, const char *unit,
                            int opt_flags, int search_flags);
# 632 "./libavutil/opt.h"
const AVOption *av_opt_find2(void *obj, const char *name, const char *unit,
                             int opt_flags, int search_flags, void **target_obj);
# 644 "./libavutil/opt.h"
const AVOption *av_opt_next(const void *obj, const AVOption *prev);







void *av_opt_child_next(void *obj, void *prev);







const AVClass *av_opt_child_class_iterate(const AVClass *parent, void **iter);
# 691 "./libavutil/opt.h"
int av_opt_set (void *obj, const char *name, const char *val, int search_flags);
int av_opt_set_int (void *obj, const char *name, int64_t val, int search_flags);
int av_opt_set_double (void *obj, const char *name, double val, int search_flags);
int av_opt_set_q (void *obj, const char *name, AVRational val, int search_flags);
int av_opt_set_bin (void *obj, const char *name, const uint8_t *val, int size, int search_flags);
int av_opt_set_image_size(void *obj, const char *name, int w, int h, int search_flags);
int av_opt_set_pixel_fmt (void *obj, const char *name, enum AVPixelFormat fmt, int search_flags);
int av_opt_set_sample_fmt(void *obj, const char *name, enum AVSampleFormat fmt, int search_flags);
int av_opt_set_video_rate(void *obj, const char *name, AVRational val, int search_flags);

__attribute__((deprecated))
int av_opt_set_channel_layout(void *obj, const char *name, int64_t ch_layout, int search_flags);

int av_opt_set_chlayout(void *obj, const char *name, const AVChannelLayout *layout, int search_flags);




int av_opt_set_dict_val(void *obj, const char *name, const AVDictionary *val, int search_flags);
# 751 "./libavutil/opt.h"
int av_opt_get (void *obj, const char *name, int search_flags, uint8_t **out_val);
int av_opt_get_int (void *obj, const char *name, int search_flags, int64_t *out_val);
int av_opt_get_double (void *obj, const char *name, int search_flags, double *out_val);
int av_opt_get_q (void *obj, const char *name, int search_flags, AVRational *out_val);
int av_opt_get_image_size(void *obj, const char *name, int search_flags, int *w_out, int *h_out);
int av_opt_get_pixel_fmt (void *obj, const char *name, int search_flags, enum AVPixelFormat *out_fmt);
int av_opt_get_sample_fmt(void *obj, const char *name, int search_flags, enum AVSampleFormat *out_fmt);
int av_opt_get_video_rate(void *obj, const char *name, int search_flags, AVRational *out_val);

__attribute__((deprecated))
int av_opt_get_channel_layout(void *obj, const char *name, int search_flags, int64_t *ch_layout);

int av_opt_get_chlayout(void *obj, const char *name, int search_flags, AVChannelLayout *layout);




int av_opt_get_dict_val(void *obj, const char *name, int search_flags, AVDictionary **out_val);
# 780 "./libavutil/opt.h"
void *av_opt_ptr(const AVClass *avclass, void *obj, const char *name);




void av_opt_freep_ranges(AVOptionRanges **ranges);
# 800 "./libavutil/opt.h"
int av_opt_query_ranges(AVOptionRanges **, void *obj, const char *key, int flags);
# 819 "./libavutil/opt.h"
int av_opt_copy(void *dest, const void *src);
# 835 "./libavutil/opt.h"
int av_opt_query_ranges_default(AVOptionRanges **, void *obj, const char *key, int flags);
# 849 "./libavutil/opt.h"
int av_opt_is_set_to_default(void *obj, const AVOption *o);
# 861 "./libavutil/opt.h"
int av_opt_is_set_to_default_by_name(void *obj, const char *name, int search_flags);
# 885 "./libavutil/opt.h"
int av_opt_serialize(void *obj, int opt_flags, int flags, char **buffer,
                     const char key_val_sep, const char pairs_sep);
# 38 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2


# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/audio.h" 1
# 25 "/Users/davidchen/repo/ffmpeg/libavfilter/audio.h"
# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h" 1
# 38 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 39 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h" 2
# 50 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
# 1 "./libavfilter/version_major.h" 1
# 51 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h" 2




# 1 "./libavfilter/version.h" 1
# 56 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h" 2





unsigned avfilter_version(void);




const char *avfilter_configuration(void);




const char *avfilter_license(void);

typedef struct AVFilterContext AVFilterContext;
typedef struct AVFilterLink AVFilterLink;
typedef struct AVFilterPad AVFilterPad;
typedef struct AVFilterFormats AVFilterFormats;
typedef struct AVFilterChannelLayouts AVFilterChannelLayouts;
# 88 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
const char *avfilter_pad_get_name(const AVFilterPad *pads, int pad_idx);
# 99 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
enum AVMediaType avfilter_pad_get_type(const AVFilterPad *pads, int pad_idx);
# 166 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
typedef struct AVFilter {



    const char *name;






    const char *description;
# 186 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    const AVFilterPad *inputs;
# 195 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    const AVFilterPad *outputs;
# 205 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    const AVClass *priv_class;




    int flags;
# 223 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    uint8_t nb_inputs;




    uint8_t nb_outputs;





    uint8_t formats_state;
# 249 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    int (*preinit)(AVFilterContext *ctx);
# 272 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    int (*init)(AVFilterContext *ctx);
# 284 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    void (*uninit)(AVFilterContext *ctx);





    union {
# 318 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
        int (*query_func)(AVFilterContext *);
# 329 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
        const enum AVPixelFormat *pixels_list;
# 340 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
        const enum AVSampleFormat *samples_list;



        enum AVPixelFormat pix_fmt;



        enum AVSampleFormat sample_fmt;
    } formats;

    int priv_size;

    int flags_internal;
# 367 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    int (*process_command)(AVFilterContext *, const char *cmd, const char *arg, char *res, int res_len, int flags);
# 381 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    int (*activate)(AVFilterContext *ctx);
} AVFilter;




unsigned avfilter_filter_pad_count(const AVFilter *filter, int is_output);






typedef struct AVFilterInternal AVFilterInternal;


struct AVFilterContext {
    const AVClass *av_class;

    const AVFilter *filter;

    char *name;

    AVFilterPad *input_pads;
    AVFilterLink **inputs;
    unsigned nb_inputs;

    AVFilterPad *output_pads;
    AVFilterLink **outputs;
    unsigned nb_outputs;

    void *priv;

    struct AVFilterGraph *graph;
# 432 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    int thread_type;




    AVFilterInternal *internal;

    struct AVFilterCommand *command_queue;

    char *enable_str;
    void *enable;
    double *var_values;
    int is_disabled;
# 457 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    AVBufferRef *hw_device_ctx;






    int nb_threads;






    unsigned ready;
# 487 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    int extra_hw_frames;
};
# 500 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
typedef struct AVFilterFormatsConfig {




    AVFilterFormats *formats;




    AVFilterFormats *samplerates;




    AVFilterChannelLayouts *channel_layouts;

} AVFilterFormatsConfig;
# 531 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
struct AVFilterLink {
    AVFilterContext *src;
    AVFilterPad *srcpad;

    AVFilterContext *dst;
    AVFilterPad *dstpad;

    enum AVMediaType type;


    int w;
    int h;
    AVRational sample_aspect_ratio;






    __attribute__((deprecated))
    uint64_t channel_layout;

    int sample_rate;

    int format;
# 564 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    AVRational time_base;

    AVChannelLayout ch_layout;
# 579 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    AVFilterFormatsConfig incfg;




    AVFilterFormatsConfig outcfg;


    enum {
        AVLINK_UNINIT = 0,
        AVLINK_STARTINIT,
        AVLINK_INIT
    } init_state;




    struct AVFilterGraph *graph;





    int64_t current_pts;





    int64_t current_pts_us;




    int age_index;
# 626 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    AVRational frame_rate;
# 635 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    int min_samples;





    int max_samples;




    int64_t frame_count_in, frame_count_out;




    int64_t sample_count_in, sample_count_out;




    void *frame_pool;






    int frame_wanted_out;





    AVBufferRef *hw_frames_ctx;
# 678 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    char reserved[0xF000];
# 715 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
};
# 726 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_link(AVFilterContext *src, unsigned srcpad,
                  AVFilterContext *dst, unsigned dstpad);




void avfilter_link_free(AVFilterLink **link);







int avfilter_config_links(AVFilterContext *filter);
# 749 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_process_command(AVFilterContext *filter, const char *cmd, const char *arg, char *res, int res_len, int flags);
# 760 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
const AVFilter *av_filter_iterate(void **opaque);
# 769 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
const AVFilter *avfilter_get_by_name(const char *name);
# 782 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_init_str(AVFilterContext *ctx, const char *args);
# 804 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_init_dict(AVFilterContext *ctx, AVDictionary **options);







void avfilter_free(AVFilterContext *filter);
# 823 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_insert_filter(AVFilterLink *link, AVFilterContext *filt,
                           unsigned filt_srcpad_idx, unsigned filt_dstpad_idx);






const AVClass *avfilter_get_class(void);

typedef struct AVFilterGraphInternal AVFilterGraphInternal;
# 847 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
typedef int (avfilter_action_func)(AVFilterContext *ctx, void *arg, int jobnr, int nb_jobs);
# 861 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
typedef int (avfilter_execute_func)(AVFilterContext *ctx, avfilter_action_func *func,
                                    void *arg, int *ret, int nb_jobs);

typedef struct AVFilterGraph {
    const AVClass *av_class;
    AVFilterContext **filters;
    unsigned nb_filters;

    char *scale_sws_opts;
# 883 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    int thread_type;






    int nb_threads;




    AVFilterGraphInternal *internal;






    void *opaque;
# 916 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    avfilter_execute_func *execute;

    char *aresample_swr_opts;
# 927 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    AVFilterLink **sink_links;
    int sink_links_count;

    unsigned disable_auto_convert;
} AVFilterGraph;






AVFilterGraph *avfilter_graph_alloc(void);
# 954 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
AVFilterContext *avfilter_graph_alloc_filter(AVFilterGraph *graph,
                                             const AVFilter *filter,
                                             const char *name);
# 966 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
AVFilterContext *avfilter_graph_get_filter(AVFilterGraph *graph, const char *name);
# 981 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_create_filter(AVFilterContext **filt_ctx, const AVFilter *filt,
                                 const char *name, const char *args, void *opaque,
                                 AVFilterGraph *graph_ctx);
# 993 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
void avfilter_graph_set_auto_convert(AVFilterGraph *graph, unsigned flags);

enum {
    AVFILTER_AUTO_CONVERT_ALL = 0,
    AVFILTER_AUTO_CONVERT_NONE = -1,
};
# 1007 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_config(AVFilterGraph *graphctx, void *log_ctx);





void avfilter_graph_free(AVFilterGraph **graph);
# 1024 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
typedef struct AVFilterInOut {

    char *name;


    AVFilterContext *filter_ctx;


    int pad_idx;


    struct AVFilterInOut *next;
} AVFilterInOut;






AVFilterInOut *avfilter_inout_alloc(void);





void avfilter_inout_free(AVFilterInOut **inout);
# 1069 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_parse(AVFilterGraph *graph, const char *filters,
                         AVFilterInOut *inputs, AVFilterInOut *outputs,
                         void *log_ctx);
# 1090 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_parse_ptr(AVFilterGraph *graph, const char *filters,
                             AVFilterInOut **inputs, AVFilterInOut **outputs,
                             void *log_ctx);
# 1116 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_parse2(AVFilterGraph *graph, const char *filters,
                          AVFilterInOut **inputs,
                          AVFilterInOut **outputs);







typedef struct AVFilterPadParams {







    char *label;
} AVFilterPadParams;







typedef struct AVFilterParams {
# 1154 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    AVFilterContext *filter;
# 1171 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    char *filter_name;
# 1183 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    char *instance_name;
# 1195 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    AVDictionary *opts;

    AVFilterPadParams **inputs;
    unsigned nb_inputs;

    AVFilterPadParams **outputs;
    unsigned nb_outputs;
} AVFilterParams;







typedef struct AVFilterChain {
    AVFilterParams **filters;
    size_t nb_filters;
} AVFilterChain;
# 1224 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
typedef struct AVFilterGraphSegment {




    AVFilterGraph *graph;





    AVFilterChain **chains;
    size_t nb_chains;
# 1246 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
    char *scale_sws_opts;
} AVFilterGraphSegment;
# 1273 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_segment_parse(AVFilterGraph *graph, const char *graph_str,
                                 int flags, AVFilterGraphSegment **seg);
# 1301 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_segment_create_filters(AVFilterGraphSegment *seg, int flags);
# 1330 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_segment_apply_opts(AVFilterGraphSegment *seg, int flags);
# 1352 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_segment_init(AVFilterGraphSegment *seg, int flags);
# 1387 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_segment_link(AVFilterGraphSegment *seg, int flags,
                                AVFilterInOut **inputs,
                                AVFilterInOut **outputs);
# 1415 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_segment_apply(AVFilterGraphSegment *seg, int flags,
                                 AVFilterInOut **inputs,
                                 AVFilterInOut **outputs);
# 1429 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
void avfilter_graph_segment_free(AVFilterGraphSegment **seg);
# 1446 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_send_command(AVFilterGraph *graph, const char *target, const char *cmd, const char *arg, char *res, int res_len, int flags);
# 1463 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_queue_command(AVFilterGraph *graph, const char *target, const char *cmd, const char *arg, int flags, double ts);
# 1474 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
char *avfilter_graph_dump(AVFilterGraph *graph, const char *options);
# 1494 "/Users/davidchen/repo/ffmpeg/libavfilter/avfilter.h"
int avfilter_graph_request_oldest(AVFilterGraph *graph);
# 26 "/Users/davidchen/repo/ffmpeg/libavfilter/audio.h" 2
# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h" 1
# 27 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
# 1 "./libavutil/internal.h" 1
# 38 "./libavutil/internal.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 39 "./libavutil/internal.h" 2
# 1 "/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/assert.h" 1 3 4
# 40 "./libavutil/internal.h" 2
# 97 "./libavutil/internal.h"
# 1 "./libavutil/libm.h" 1
# 98 "./libavutil/internal.h" 2
# 116 "./libavutil/internal.h"
void avpriv_report_missing_feature(void *avc,
                                   const char *msg, ...) __attribute__((__format__(__printf__, 2, 3)));
# 127 "./libavutil/internal.h"
void avpriv_request_sample(void *avc,
                           const char *msg, ...) __attribute__((__format__(__printf__, 2, 3)));
# 166 "./libavutil/internal.h"
int avpriv_set_systematic_pal2(uint32_t pal[256], enum AVPixelFormat pix_fmt);

static __attribute__((always_inline)) inline __attribute__((const)) int avpriv_mirror(int x, int w)
{
    if (!w)
        return 0;

    while ((unsigned)x > (unsigned)w) {
        x = -x;
        if (x < 0)
            x += 2 * w;
    }
    return x;
}
# 28 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h" 2

# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/framequeue.h" 1
# 34 "/Users/davidchen/repo/ffmpeg/libavfilter/framequeue.h"
typedef struct FFFrameBucket {
    AVFrame *frame;
} FFFrameBucket;
# 46 "/Users/davidchen/repo/ffmpeg/libavfilter/framequeue.h"
typedef struct FFFrameQueueGlobal {
    char dummy;
} FFFrameQueueGlobal;




typedef struct FFFrameQueue {




    FFFrameBucket *queue;




    size_t allocated;





    size_t tail;




    size_t queued;




    FFFrameBucket first_bucket;




    uint64_t total_frames_head;





    uint64_t total_frames_tail;




    uint64_t total_samples_head;





    uint64_t total_samples_tail;




    int samples_skipped;

} FFFrameQueue;




void ff_framequeue_global_init(FFFrameQueueGlobal *fqg);




void ff_framequeue_init(FFFrameQueue *fq, FFFrameQueueGlobal *fqg);




void ff_framequeue_free(FFFrameQueue *fq);





int ff_framequeue_add(FFFrameQueue *fq, AVFrame *frame);





AVFrame *ff_framequeue_take(FFFrameQueue *fq);





AVFrame *ff_framequeue_peek(FFFrameQueue *fq, size_t idx);




static inline size_t ff_framequeue_queued_frames(const FFFrameQueue *fq)
{
    return fq->queued;
}




static inline uint64_t ff_framequeue_queued_samples(const FFFrameQueue *fq)
{
    return fq->total_samples_head - fq->total_samples_tail;
}






static inline void ff_framequeue_update_peeked(FFFrameQueue *fq, size_t idx)
{
}
# 176 "/Users/davidchen/repo/ffmpeg/libavfilter/framequeue.h"
void ff_framequeue_skip_samples(FFFrameQueue *fq, size_t samples, AVRational time_base);
# 30 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h" 2

typedef struct AVFilterCommand {
    double time;
    char *command;
    char *arg;
    int flags;
    struct AVFilterCommand *next;
} AVFilterCommand;




void ff_avfilter_graph_update_heap(AVFilterGraph *graph, AVFilterLink *link);




struct AVFilterPad {





    const char *name;




    enum AVMediaType type;
# 76 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
    int flags;
# 87 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
    union {
        AVFrame *(*video)(AVFilterLink *link, int w, int h);
        AVFrame *(*audio)(AVFilterLink *link, int nb_samples);
    } get_buffer;
# 102 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
    int (*filter_frame)(AVFilterLink *link, AVFrame *frame);
# 111 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
    int (*request_frame)(AVFilterLink *link);
# 127 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
    int (*config_props)(AVFilterLink *link);
};

struct AVFilterGraphInternal {
    void *thread;
    avfilter_execute_func *thread_execute;
    FFFrameQueueGlobal frame_queues;
};

struct AVFilterInternal {
    avfilter_execute_func *execute;



    int initialized;
};

static __attribute__((always_inline)) inline int ff_filter_execute(AVFilterContext *ctx, avfilter_action_func *func,
                                              void *arg, int *ret, int nb_jobs)
{
    return ctx->internal->execute(ctx, func, arg, ret, nb_jobs);
}

enum FilterFormatsState {
# 161 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
    FF_FILTER_FORMATS_PASSTHROUGH = 0,
    FF_FILTER_FORMATS_QUERY_FUNC,
    FF_FILTER_FORMATS_PIXFMT_LIST,
    FF_FILTER_FORMATS_SAMPLEFMTS_LIST,
    FF_FILTER_FORMATS_SINGLE_PIXFMT,
    FF_FILTER_FORMATS_SINGLE_SAMPLEFMT,
};
# 204 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
int ff_fmt_is_in(int fmt, const int *fmts);
# 216 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
__attribute__((warn_unused_result))
int ff_parse_pixel_format(enum AVPixelFormat *ret, const char *arg, void *log_ctx);
# 227 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
__attribute__((warn_unused_result))
int ff_parse_sample_rate(int *ret, const char *arg, void *log_ctx);
# 240 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
__attribute__((warn_unused_result))
int ff_parse_channel_layout(AVChannelLayout *ret, int *nret, const char *arg,
                            void *log_ctx);
# 251 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
void ff_avfilter_link_set_in_status(AVFilterLink *link, int status, int64_t pts);
# 273 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
int ff_append_inpad (AVFilterContext *f, AVFilterPad *p);
int ff_append_outpad(AVFilterContext *f, AVFilterPad *p);
int ff_append_inpad_free_name (AVFilterContext *f, AVFilterPad *p);
int ff_append_outpad_free_name(AVFilterContext *f, AVFilterPad *p);
# 309 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
int ff_request_frame(AVFilterLink *link);
# 341 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
int ff_filter_frame(AVFilterLink *link, AVFrame *frame);
# 351 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
AVFilterContext *ff_filter_alloc(const AVFilter *filter, const char *inst_name);

int ff_filter_activate(AVFilterContext *filter);




void ff_filter_graph_remove_filter(AVFilterGraph *graph, AVFilterContext *filter);
# 369 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
int ff_filter_graph_run_once(AVFilterGraph *graph);





int ff_filter_get_nb_threads(AVFilterContext *ctx) __attribute__((pure));







int ff_filter_process_command(AVFilterContext *ctx, const char *cmd,
                              const char *arg, char *res, int res_len, int flags);
# 399 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
int ff_filter_init_hw_frames(AVFilterContext *avctx, AVFilterLink *link,
                             int default_pool_size);
# 412 "/Users/davidchen/repo/ffmpeg/libavfilter/internal.h"
int ff_filter_opt_parse(void *logctx, const AVClass *priv_class,
                        AVDictionary **options, const char *args);
# 27 "/Users/davidchen/repo/ffmpeg/libavfilter/audio.h" 2





extern const AVFilterPad ff_audio_default_filterpad[1];


AVFrame *ff_default_get_audio_buffer(AVFilterLink *link, int nb_samples);


AVFrame *ff_null_get_audio_buffer(AVFilterLink *link, int nb_samples);
# 48 "/Users/davidchen/repo/ffmpeg/libavfilter/audio.h"
AVFrame *ff_get_audio_buffer(AVFilterLink *link, int nb_samples);
# 41 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2

# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/filters.h" 1
# 46 "/Users/davidchen/repo/ffmpeg/libavfilter/filters.h"
void ff_filter_set_ready(AVFilterContext *filter, unsigned priority);






int ff_inlink_process_commands(AVFilterLink *link, const AVFrame *frame);







int ff_inlink_evaluate_timeline_at_frame(AVFilterLink *link, const AVFrame *frame);





size_t ff_inlink_queued_frames(AVFilterLink *link);





int ff_inlink_check_available_frame(AVFilterLink *link);






int ff_inlink_queued_samples(AVFilterLink *link);






int ff_inlink_check_available_samples(AVFilterLink *link, unsigned min);
# 101 "/Users/davidchen/repo/ffmpeg/libavfilter/filters.h"
int ff_inlink_consume_frame(AVFilterLink *link, AVFrame **rframe);
# 115 "/Users/davidchen/repo/ffmpeg/libavfilter/filters.h"
int ff_inlink_consume_samples(AVFilterLink *link, unsigned min, unsigned max,
                            AVFrame **rframe);






AVFrame *ff_inlink_peek_frame(AVFilterLink *link, size_t idx);






int ff_inlink_make_frame_writable(AVFilterLink *link, AVFrame **rframe);
# 153 "/Users/davidchen/repo/ffmpeg/libavfilter/filters.h"
int ff_inlink_acknowledge_status(AVFilterLink *link, int *rstatus, int64_t *rpts);







void ff_inlink_request_frame(AVFilterLink *link);





void ff_inlink_set_status(AVFilterLink *link, int status);




static inline int ff_outlink_frame_wanted(AVFilterLink *link)
{
    return link->frame_wanted_out;
}




int ff_outlink_get_status(AVFilterLink *link);
# 189 "/Users/davidchen/repo/ffmpeg/libavfilter/filters.h"
static inline void ff_outlink_set_status(AVFilterLink *link, int status, int64_t pts)
{
    ff_avfilter_link_set_in_status(link, status, pts);
}
# 267 "/Users/davidchen/repo/ffmpeg/libavfilter/filters.h"
int ff_inoutlink_check_flow(AVFilterLink *inlink, AVFilterLink *outlink);
# 43 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2
# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h" 1
# 64 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h"
struct AVFilterFormats {
    unsigned nb_formats;
    int *formats;

    unsigned refcount;
    struct AVFilterFormats ***refs;
};
# 85 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h"
struct AVFilterChannelLayouts {
    AVChannelLayout *channel_layouts;
    int nb_channel_layouts;
    char all_layouts;
    char all_counts;

    unsigned refcount;
    struct AVFilterChannelLayouts ***refs;
};
# 117 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h"
__attribute__((warn_unused_result))
AVFilterChannelLayouts *ff_all_channel_layouts(void);

__attribute__((warn_unused_result))
AVFilterFormats *ff_all_samplerates(void);





__attribute__((warn_unused_result))
AVFilterChannelLayouts *ff_all_channel_counts(void);

__attribute__((warn_unused_result))
AVFilterChannelLayouts *ff_make_channel_layout_list(const AVChannelLayout *fmts);






__attribute__((warn_unused_result))
int ff_set_common_channel_layouts(AVFilterContext *ctx,
                                  AVFilterChannelLayouts *layouts);



__attribute__((warn_unused_result))
int ff_set_common_channel_layouts_from_list(AVFilterContext *ctx,
                                            const AVChannelLayout *fmts);



__attribute__((warn_unused_result))
int ff_set_common_all_channel_counts(AVFilterContext *ctx);

__attribute__((warn_unused_result))
int ff_set_common_samplerates(AVFilterContext *ctx,
                              AVFilterFormats *samplerates);



__attribute__((warn_unused_result))
int ff_set_common_samplerates_from_list(AVFilterContext *ctx,
                                        const int *samplerates);



__attribute__((warn_unused_result))
int ff_set_common_all_samplerates(AVFilterContext *ctx);






__attribute__((warn_unused_result))
int ff_set_common_formats(AVFilterContext *ctx, AVFilterFormats *formats);




__attribute__((warn_unused_result))
int ff_set_common_formats_from_list(AVFilterContext *ctx, const int *fmts);

__attribute__((warn_unused_result))
int ff_add_channel_layout(AVFilterChannelLayouts **l,
                          const AVChannelLayout *channel_layout);




__attribute__((warn_unused_result))
int ff_channel_layouts_ref(AVFilterChannelLayouts *f,
                           AVFilterChannelLayouts **ref);




void ff_channel_layouts_unref(AVFilterChannelLayouts **ref);

void ff_channel_layouts_changeref(AVFilterChannelLayouts **oldref,
                                  AVFilterChannelLayouts **newref);

__attribute__((warn_unused_result))
int ff_default_query_formats(AVFilterContext *ctx);
# 211 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h"
__attribute__((warn_unused_result))
AVFilterFormats *ff_make_format_list(const int *fmts);




__attribute__((warn_unused_result))
AVFilterFormats *ff_make_formats_list_singleton(int fmt);
# 228 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h"
__attribute__((warn_unused_result))
int ff_add_format(AVFilterFormats **avff, int64_t fmt);




__attribute__((warn_unused_result))
AVFilterFormats *ff_all_formats(enum AVMediaType type);





__attribute__((warn_unused_result))
AVFilterFormats *ff_formats_pixdesc_filter(unsigned want, unsigned rej);







__attribute__((warn_unused_result))
AVFilterFormats *ff_planar_sample_fmts(void);
# 265 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h"
__attribute__((warn_unused_result))
int ff_formats_ref(AVFilterFormats *formats, AVFilterFormats **ref);
# 283 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h"
void ff_formats_unref(AVFilterFormats **ref);
# 297 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h"
void ff_formats_changeref(AVFilterFormats **oldref, AVFilterFormats **newref);






int ff_formats_check_pixel_formats(void *log, const AVFilterFormats *fmts);






int ff_formats_check_sample_formats(void *log, const AVFilterFormats *fmts);






int ff_formats_check_sample_rates(void *log, const AVFilterFormats *fmts);






int ff_formats_check_channel_layouts(void *log, const AVFilterChannelLayouts *fmts);

typedef struct AVFilterFormatMerger {
    unsigned offset;
    int (*merge)(void *a, void *b);
    int (*can_merge)(const void *a, const void *b);
} AVFilterFormatsMerger;
# 418 "/Users/davidchen/repo/ffmpeg/libavfilter/formats.h"
typedef struct AVFilterNegotiation {
    unsigned nb_mergers;
    const AVFilterFormatsMerger *mergers;
    const char *conversion_filter;
    unsigned conversion_opts_offset;
} AVFilterNegotiation;

const AVFilterNegotiation *ff_filter_get_negotiation(AVFilterLink *link);
# 44 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2

# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.h" 1
# 29 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.h"
# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afirdsp.h" 1
# 24 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afirdsp.h"
# 1 "/Library/Developer/CommandLineTools/usr/lib/clang/15.0.0/include/stddef.h" 1 3
# 25 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afirdsp.h" 2




typedef struct AudioFIRDSPContext {
    void (*fcmul_add)(float *sum, const float *t, const float *c,
                      ptrdiff_t len);
    void (*dcmul_add)(double *sum, const double *t, const double *c,
                      ptrdiff_t len);
} AudioFIRDSPContext;

void ff_afir_init_riscv(AudioFIRDSPContext *s);
void ff_afir_init_x86(AudioFIRDSPContext *s);

static void fcmul_add_c(float *sum, const float *t, const float *c, ptrdiff_t len)
{
    int n;

    for (n = 0; n < len; n++) {
        const float cre = c[2 * n ];
        const float cim = c[2 * n + 1];
        const float tre = t[2 * n ];
        const float tim = t[2 * n + 1];

        sum[2 * n ] += tre * cre - tim * cim;
        sum[2 * n + 1] += tre * cim + tim * cre;
    }

    sum[2 * n] += t[2 * n] * c[2 * n];
}

static void dcmul_add_c(double *sum, const double *t, const double *c, ptrdiff_t len)
{
    int n;

    for (n = 0; n < len; n++) {
        const double cre = c[2 * n ];
        const double cim = c[2 * n + 1];
        const double tre = t[2 * n ];
        const double tim = t[2 * n + 1];

        sum[2 * n ] += tre * cre - tim * cim;
        sum[2 * n + 1] += tre * cim + tim * cre;
    }

    sum[2 * n] += t[2 * n] * c[2 * n];
}

static __attribute__((unused)) void ff_afir_init(AudioFIRDSPContext *dsp)
{
    dsp->fcmul_add = fcmul_add_c;
    dsp->dcmul_add = dcmul_add_c;






}
# 30 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.h" 2



typedef struct AudioFIRSegment {
    int nb_partitions;
    int part_size;
    int block_size;
    int fft_length;
    int coeff_size;
    int input_size;
    int input_offset;

    int *output_offset;
    int *part_index;

    AVFrame *sumin;
    AVFrame *sumout;
    AVFrame *blockout;
    AVFrame *tempin;
    AVFrame *tempout;
    AVFrame *buffer;
    AVFrame *coeff;
    AVFrame *input;
    AVFrame *output;

    AVTXContext **ctx, **tx, **itx;
    av_tx_fn ctx_fn, tx_fn, itx_fn;
} AudioFIRSegment;

typedef struct AudioFIRContext {
    const AVClass *class;

    float wet_gain;
    float dry_gain;
    float length;
    int gtype;
    float ir_norm;
    float ir_link;
    float ir_gain;
    int ir_format;
    int ir_load;
    float max_ir_len;
    int response;
    int w, h;
    AVRational frame_rate;
    int ir_channel;
    int minp;
    int maxp;
    int nb_irs;
    int prev_selir;
    int selir;
    int precision;
    int format;

    int eof_coeffs[32];
    int have_coeffs[32];
    int nb_taps[32];
    int nb_segments[32];
    int max_offset[32];
    int nb_channels;
    int one2many;
    int prev_is_disabled;
    int *loading;
    double *ch_gain;

    AudioFIRSegment seg[32][1024];

    AVFrame *in;
    AVFrame *xfade[2];
    AVFrame *fadein[2];
    AVFrame *ir[32];
    AVFrame *norm_ir[32];
    int min_part_size;
    int max_part_size;
    int64_t pts;

    AudioFIRDSPContext afirdsp;
    AVFloatDSPContext *fdsp;
} AudioFIRContext;
# 46 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2

# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/video.h" 1
# 31 "/Users/davidchen/repo/ffmpeg/libavfilter/video.h"
extern const AVFilterPad ff_video_default_filterpad[1];

AVFrame *ff_default_get_video_buffer(AVFilterLink *link, int w, int h);
AVFrame *ff_default_get_video_buffer2(AVFilterLink *link, int w, int h, int align);
AVFrame *ff_null_get_video_buffer(AVFilterLink *link, int w, int h);
# 46 "/Users/davidchen/repo/ffmpeg/libavfilter/video.h"
AVFrame *ff_get_video_buffer(AVFilterLink *link, int w, int h);
# 48 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2


# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/afir_template.c" 1
# 58 "/Users/davidchen/repo/ffmpeg/libavfilter/afir_template.c"
static float ir_gain_float(AVFilterContext *ctx, AudioFIRContext *s,
                         int cur_nb_taps, const float *time)
{
    float ch_gain, sum = 0;

    if (s->ir_norm < 0.f) {
        ch_gain = 1;
    } else if (s->ir_norm == 0.f) {
        for (int i = 0; i < cur_nb_taps; i++)
            sum += time[i];
        ch_gain = 1. / sum;
    } else {
        float ir_norm = s->ir_norm;

        for (int i = 0; i < cur_nb_taps; i++)
            sum += powf(fabsf(time[i]), ir_norm);
        ch_gain = 1. / powf(sum, 1. / ir_norm);
    }

    return ch_gain;
}

static void ir_scale_float(AVFilterContext *ctx, AudioFIRContext *s,
                         int cur_nb_taps, int ch,
                         float *time, float ch_gain)
{
    if (ch_gain != 1. || s->ir_gain != 1.) {
        float gain = ch_gain * s->ir_gain;

        av_log(ctx, 48, "ch%d gain %f\n", ch, gain);

        s->fdsp->vector_fmul_scalar(time, time, gain, (((cur_nb_taps)+(4)-1)&~((4)-1)));



    }
}

static void convert_channel_float(AVFilterContext *ctx, AudioFIRContext *s, int ch,
                                AudioFIRSegment *seg, int coeff_partition, int selir)
{
    const int coffset = coeff_partition * seg->coeff_size;
    const int nb_taps = s->nb_taps[selir];
    float *time = (float *)s->norm_ir[selir]->extended_data[ch];
    float *tempin = (float *)seg->tempin->extended_data[ch];
    float *tempout = (float *)seg->tempout->extended_data[ch];
    AVComplexFloat *coeff = (AVComplexFloat *)seg->coeff->extended_data[ch];
    const int remaining = nb_taps - (seg->input_offset + coeff_partition * seg->part_size);
    const int size = remaining >= seg->part_size ? seg->part_size : remaining;

    __builtin___memset_chk (tempin + size, 0, sizeof(*tempin) * (seg->block_size - size), __builtin_object_size (tempin + size, 0));
    __builtin___memcpy_chk (tempin, time + seg->input_offset + coeff_partition * seg->part_size, size * sizeof(*tempin), __builtin_object_size (tempin, 0));

    seg->ctx_fn(seg->ctx[ch], tempout, tempin, sizeof(*tempin));
    __builtin___memcpy_chk (coeff + coffset, tempout, seg->coeff_size * sizeof(*coeff), __builtin_object_size (coeff + coffset, 0));

    av_log(ctx, 48, "channel: %d\n", ch);
    av_log(ctx, 48, "nb_partitions: %d\n", seg->nb_partitions);
    av_log(ctx, 48, "partition size: %d\n", seg->part_size);
    av_log(ctx, 48, "block size: %d\n", seg->block_size);
    av_log(ctx, 48, "fft_length: %d\n", seg->fft_length);
    av_log(ctx, 48, "coeff_size: %d\n", seg->coeff_size);
    av_log(ctx, 48, "input_size: %d\n", seg->input_size);
    av_log(ctx, 48, "input_offset: %d\n", seg->input_offset);
}

static void fir_fadd_float(AudioFIRContext *s, float *dst, const float *src, int nb_samples)
{
    if ((nb_samples & 15) == 0 && nb_samples >= 8) {

        s->fdsp->vector_fmac_scalar(dst, src, 1.f, nb_samples);



    } else {
        for (int n = 0; n < nb_samples; n++)
            dst[n] += src[n];
    }
}

static int fir_quantum_float(AVFilterContext *ctx, AVFrame *out, int ch, int ioffset, int offset, int selir)
{
    AudioFIRContext *s = ctx->priv;
    const float *in = (const float *)s->in->extended_data[ch] + ioffset;
    float *blockout, *ptr = (float *)out->extended_data[ch] + offset;
    const int min_part_size = s->min_part_size;
    const int nb_samples = ((min_part_size) > (out->nb_samples - offset) ? (out->nb_samples - offset) : (min_part_size));
    const int nb_segments = s->nb_segments[selir];
    const float dry_gain = s->dry_gain;
    const float wet_gain = s->wet_gain;

    for (int segment = 0; segment < nb_segments; segment++) {
        AudioFIRSegment *seg = &s->seg[selir][segment];
        float *src = (float *)seg->input->extended_data[ch];
        float *dst = (float *)seg->output->extended_data[ch];
        float *sumin = (float *)seg->sumin->extended_data[ch];
        float *sumout = (float *)seg->sumout->extended_data[ch];
        float *tempin = (float *)seg->tempin->extended_data[ch];
        float *buf = (float *)seg->buffer->extended_data[ch];
        int *output_offset = &seg->output_offset[ch];
        const int nb_partitions = seg->nb_partitions;
        const int input_offset = seg->input_offset;
        const int part_size = seg->part_size;
        int j;

        seg->part_index[ch] = seg->part_index[ch] % nb_partitions;
        if (dry_gain == 1.f) {
            __builtin___memcpy_chk (src + input_offset, in, nb_samples * sizeof(*src), __builtin_object_size (src + input_offset, 0));
        } else if (min_part_size >= 8) {

            s->fdsp->vector_fmul_scalar(src + input_offset, in, dry_gain, (((nb_samples)+(4)-1)&~((4)-1)));



        } else {
            float *src2 = src + input_offset;
            for (int n = 0; n < nb_samples; n++)
                src2[n] = in[n] * dry_gain;
        }

        output_offset[0] += min_part_size;
        if (output_offset[0] >= part_size) {
            output_offset[0] = 0;
        } else {
            __builtin___memmove_chk (src, src + min_part_size, (seg->input_size - min_part_size) * sizeof(*src), __builtin_object_size (src, 0));

            dst += output_offset[0];
            fir_fadd_float(s, ptr, dst, nb_samples);
            continue;
        }

        __builtin___memset_chk (sumin, 0, sizeof(*sumin) * seg->fft_length, __builtin_object_size (sumin, 0));

        blockout = (float *)seg->blockout->extended_data[ch] + seg->part_index[ch] * seg->block_size;
        __builtin___memset_chk (tempin + part_size, 0, sizeof(*tempin) * (seg->block_size - part_size), __builtin_object_size (tempin + part_size, 0));
        __builtin___memcpy_chk (tempin, src, sizeof(*src) * part_size, __builtin_object_size (tempin, 0));
        seg->tx_fn(seg->tx[ch], blockout, tempin, sizeof(float));

        j = seg->part_index[ch];
        for (int i = 0; i < nb_partitions; i++) {
            const int input_partition = j;
            const int coeff_partition = i;
            const int coffset = coeff_partition * seg->coeff_size;
            const float *blockout = (const float *)seg->blockout->extended_data[ch] + input_partition * seg->block_size;
            const AVComplexFloat *coeff = ((const AVComplexFloat *)seg->coeff->extended_data[ch]) + coffset;

            if (j == 0)
                j = nb_partitions;
            j--;


            s->afirdsp.fcmul_add(sumin, blockout, (const float *)coeff, part_size);



        }

        seg->itx_fn(seg->itx[ch], sumout, sumin, sizeof(AVComplexFloat));

        fir_fadd_float(s, buf, sumout, part_size);
        __builtin___memcpy_chk (dst, buf, part_size * sizeof(*dst), __builtin_object_size (dst, 0));
        __builtin___memcpy_chk (buf, sumout + part_size, part_size * sizeof(*buf), __builtin_object_size (buf, 0));

        fir_fadd_float(s, ptr, dst, nb_samples);

        if (part_size != min_part_size)
            __builtin___memmove_chk (src, src + min_part_size, (seg->input_size - min_part_size) * sizeof(*src), __builtin_object_size (src, 0));

        seg->part_index[ch] = (seg->part_index[ch] + 1) % nb_partitions;
    }

    if (wet_gain == 1.f)
        return 0;

    if (min_part_size >= 8) {

        s->fdsp->vector_fmul_scalar(ptr, ptr, wet_gain, (((nb_samples)+(4)-1)&~((4)-1)));



    } else {
        for (int n = 0; n < nb_samples; n++)
            ptr[n] *= wet_gain;
    }

    return 0;
}

static void fir_quantums_float(AVFilterContext *ctx, AudioFIRContext *s, AVFrame *out,
                             int min_part_size, int ch, int offset,
                             int prev_selir, int selir)
{
    if (ctx->is_disabled || s->prev_is_disabled) {
        const float *in = (const float *)s->in->extended_data[ch] + offset;
        const float *xfade0 = (const float *)s->xfade[0]->extended_data[ch];
        const float *xfade1 = (const float *)s->xfade[1]->extended_data[ch];
        float *src0 = (float *)s->fadein[0]->extended_data[ch];
        float *src1 = (float *)s->fadein[1]->extended_data[ch];
        float *dst = ((float *)out->extended_data[ch]) + offset;

        if (ctx->is_disabled && !s->prev_is_disabled) {
            __builtin___memset_chk (src0, 0, min_part_size * sizeof(float), __builtin_object_size (src0, 0));
            fir_quantum_float(ctx, s->fadein[0], ch, offset, 0, selir);
            for (int n = 0; n < min_part_size; n++)
                dst[n] = xfade1[n] * src0[n] + xfade0[n] * in[n];
        } else if (!ctx->is_disabled && s->prev_is_disabled) {
            __builtin___memset_chk (src1, 0, min_part_size * sizeof(float), __builtin_object_size (src1, 0));
            fir_quantum_float(ctx, s->fadein[1], ch, offset, 0, selir);
            for (int n = 0; n < min_part_size; n++)
                dst[n] = xfade1[n] * in[n] + xfade0[n] * src1[n];
        } else {
            __builtin___memcpy_chk (dst, in, sizeof(float) * min_part_size, __builtin_object_size (dst, 0));
        }
    } else if (prev_selir != selir && s->loading[ch] != 0) {
        const float *xfade0 = (const float *)s->xfade[0]->extended_data[ch];
        const float *xfade1 = (const float *)s->xfade[1]->extended_data[ch];
        float *src0 = (float *)s->fadein[0]->extended_data[ch];
        float *src1 = (float *)s->fadein[1]->extended_data[ch];
        float *dst = ((float *)out->extended_data[ch]) + offset;

        __builtin___memset_chk (src0, 0, min_part_size * sizeof(float), __builtin_object_size (src0, 0));
        __builtin___memset_chk (src1, 0, min_part_size * sizeof(float), __builtin_object_size (src1, 0));

        fir_quantum_float(ctx, s->fadein[0], ch, offset, 0, prev_selir);
        fir_quantum_float(ctx, s->fadein[1], ch, offset, 0, selir);

        if (s->loading[ch] > s->max_offset[selir]) {
            for (int n = 0; n < min_part_size; n++)
                dst[n] = xfade1[n] * src0[n] + xfade0[n] * src1[n];
            s->loading[ch] = 0;
        } else {
            __builtin___memcpy_chk (dst, src0, min_part_size * sizeof(float), __builtin_object_size (dst, 0));
        }
    } else {
        fir_quantum_float(ctx, out, ch, offset, offset, selir);
    }
}
# 51 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2



# 1 "/Users/davidchen/repo/ffmpeg/libavfilter/afir_template.c" 1
# 58 "/Users/davidchen/repo/ffmpeg/libavfilter/afir_template.c"
static double ir_gain_double(AVFilterContext *ctx, AudioFIRContext *s,
                         int cur_nb_taps, const double *time)
{
    double ch_gain, sum = 0;

    if (s->ir_norm < 0.f) {
        ch_gain = 1;
    } else if (s->ir_norm == 0.f) {
        for (int i = 0; i < cur_nb_taps; i++)
            sum += time[i];
        ch_gain = 1. / sum;
    } else {
        double ir_norm = s->ir_norm;

        for (int i = 0; i < cur_nb_taps; i++)
            sum += pow(fabs(time[i]), ir_norm);
        ch_gain = 1. / pow(sum, 1. / ir_norm);
    }

    return ch_gain;
}

static void ir_scale_double(AVFilterContext *ctx, AudioFIRContext *s,
                         int cur_nb_taps, int ch,
                         double *time, double ch_gain)
{
    if (ch_gain != 1. || s->ir_gain != 1.) {
        double gain = ch_gain * s->ir_gain;

        av_log(ctx, 48, "ch%d gain %f\n", ch, gain);



        s->fdsp->vector_dmul_scalar(time, time, gain, (((cur_nb_taps)+(8)-1)&~((8)-1)));

    }
}

static void convert_channel_double(AVFilterContext *ctx, AudioFIRContext *s, int ch,
                                AudioFIRSegment *seg, int coeff_partition, int selir)
{
    const int coffset = coeff_partition * seg->coeff_size;
    const int nb_taps = s->nb_taps[selir];
    double *time = (double *)s->norm_ir[selir]->extended_data[ch];
    double *tempin = (double *)seg->tempin->extended_data[ch];
    double *tempout = (double *)seg->tempout->extended_data[ch];
    AVComplexDouble *coeff = (AVComplexDouble *)seg->coeff->extended_data[ch];
    const int remaining = nb_taps - (seg->input_offset + coeff_partition * seg->part_size);
    const int size = remaining >= seg->part_size ? seg->part_size : remaining;

    __builtin___memset_chk (tempin + size, 0, sizeof(*tempin) * (seg->block_size - size), __builtin_object_size (tempin + size, 0));
    __builtin___memcpy_chk (tempin, time + seg->input_offset + coeff_partition * seg->part_size, size * sizeof(*tempin), __builtin_object_size (tempin, 0));

    seg->ctx_fn(seg->ctx[ch], tempout, tempin, sizeof(*tempin));
    __builtin___memcpy_chk (coeff + coffset, tempout, seg->coeff_size * sizeof(*coeff), __builtin_object_size (coeff + coffset, 0));

    av_log(ctx, 48, "channel: %d\n", ch);
    av_log(ctx, 48, "nb_partitions: %d\n", seg->nb_partitions);
    av_log(ctx, 48, "partition size: %d\n", seg->part_size);
    av_log(ctx, 48, "block size: %d\n", seg->block_size);
    av_log(ctx, 48, "fft_length: %d\n", seg->fft_length);
    av_log(ctx, 48, "coeff_size: %d\n", seg->coeff_size);
    av_log(ctx, 48, "input_size: %d\n", seg->input_size);
    av_log(ctx, 48, "input_offset: %d\n", seg->input_offset);
}

static void fir_fadd_double(AudioFIRContext *s, double *dst, const double *src, int nb_samples)
{
    if ((nb_samples & 15) == 0 && nb_samples >= 8) {



        s->fdsp->vector_dmac_scalar(dst, src, 1.0, nb_samples);

    } else {
        for (int n = 0; n < nb_samples; n++)
            dst[n] += src[n];
    }
}

static int fir_quantum_double(AVFilterContext *ctx, AVFrame *out, int ch, int ioffset, int offset, int selir)
{
    AudioFIRContext *s = ctx->priv;
    const double *in = (const double *)s->in->extended_data[ch] + ioffset;
    double *blockout, *ptr = (double *)out->extended_data[ch] + offset;
    const int min_part_size = s->min_part_size;
    const int nb_samples = ((min_part_size) > (out->nb_samples - offset) ? (out->nb_samples - offset) : (min_part_size));
    const int nb_segments = s->nb_segments[selir];
    const float dry_gain = s->dry_gain;
    const float wet_gain = s->wet_gain;

    for (int segment = 0; segment < nb_segments; segment++) {
        AudioFIRSegment *seg = &s->seg[selir][segment];
        double *src = (double *)seg->input->extended_data[ch];
        double *dst = (double *)seg->output->extended_data[ch];
        double *sumin = (double *)seg->sumin->extended_data[ch];
        double *sumout = (double *)seg->sumout->extended_data[ch];
        double *tempin = (double *)seg->tempin->extended_data[ch];
        double *buf = (double *)seg->buffer->extended_data[ch];
        int *output_offset = &seg->output_offset[ch];
        const int nb_partitions = seg->nb_partitions;
        const int input_offset = seg->input_offset;
        const int part_size = seg->part_size;
        int j;

        seg->part_index[ch] = seg->part_index[ch] % nb_partitions;
        if (dry_gain == 1.f) {
            __builtin___memcpy_chk (src + input_offset, in, nb_samples * sizeof(*src), __builtin_object_size (src + input_offset, 0));
        } else if (min_part_size >= 8) {



            s->fdsp->vector_dmul_scalar(src + input_offset, in, dry_gain, (((nb_samples)+(8)-1)&~((8)-1)));

        } else {
            double *src2 = src + input_offset;
            for (int n = 0; n < nb_samples; n++)
                src2[n] = in[n] * dry_gain;
        }

        output_offset[0] += min_part_size;
        if (output_offset[0] >= part_size) {
            output_offset[0] = 0;
        } else {
            __builtin___memmove_chk (src, src + min_part_size, (seg->input_size - min_part_size) * sizeof(*src), __builtin_object_size (src, 0));

            dst += output_offset[0];
            fir_fadd_double(s, ptr, dst, nb_samples);
            continue;
        }

        __builtin___memset_chk (sumin, 0, sizeof(*sumin) * seg->fft_length, __builtin_object_size (sumin, 0));

        blockout = (double *)seg->blockout->extended_data[ch] + seg->part_index[ch] * seg->block_size;
        __builtin___memset_chk (tempin + part_size, 0, sizeof(*tempin) * (seg->block_size - part_size), __builtin_object_size (tempin + part_size, 0));
        __builtin___memcpy_chk (tempin, src, sizeof(*src) * part_size, __builtin_object_size (tempin, 0));
        seg->tx_fn(seg->tx[ch], blockout, tempin, sizeof(double));

        j = seg->part_index[ch];
        for (int i = 0; i < nb_partitions; i++) {
            const int input_partition = j;
            const int coeff_partition = i;
            const int coffset = coeff_partition * seg->coeff_size;
            const double *blockout = (const double *)seg->blockout->extended_data[ch] + input_partition * seg->block_size;
            const AVComplexDouble *coeff = ((const AVComplexDouble *)seg->coeff->extended_data[ch]) + coffset;

            if (j == 0)
                j = nb_partitions;
            j--;




            s->afirdsp.dcmul_add(sumin, blockout, (const double *)coeff, part_size);

        }

        seg->itx_fn(seg->itx[ch], sumout, sumin, sizeof(AVComplexDouble));

        fir_fadd_double(s, buf, sumout, part_size);
        __builtin___memcpy_chk (dst, buf, part_size * sizeof(*dst), __builtin_object_size (dst, 0));
        __builtin___memcpy_chk (buf, sumout + part_size, part_size * sizeof(*buf), __builtin_object_size (buf, 0));

        fir_fadd_double(s, ptr, dst, nb_samples);

        if (part_size != min_part_size)
            __builtin___memmove_chk (src, src + min_part_size, (seg->input_size - min_part_size) * sizeof(*src), __builtin_object_size (src, 0));

        seg->part_index[ch] = (seg->part_index[ch] + 1) % nb_partitions;
    }

    if (wet_gain == 1.f)
        return 0;

    if (min_part_size >= 8) {



        s->fdsp->vector_dmul_scalar(ptr, ptr, wet_gain, (((nb_samples)+(8)-1)&~((8)-1)));

    } else {
        for (int n = 0; n < nb_samples; n++)
            ptr[n] *= wet_gain;
    }

    return 0;
}

static void fir_quantums_double(AVFilterContext *ctx, AudioFIRContext *s, AVFrame *out,
                             int min_part_size, int ch, int offset,
                             int prev_selir, int selir)
{
    if (ctx->is_disabled || s->prev_is_disabled) {
        const double *in = (const double *)s->in->extended_data[ch] + offset;
        const double *xfade0 = (const double *)s->xfade[0]->extended_data[ch];
        const double *xfade1 = (const double *)s->xfade[1]->extended_data[ch];
        double *src0 = (double *)s->fadein[0]->extended_data[ch];
        double *src1 = (double *)s->fadein[1]->extended_data[ch];
        double *dst = ((double *)out->extended_data[ch]) + offset;

        if (ctx->is_disabled && !s->prev_is_disabled) {
            __builtin___memset_chk (src0, 0, min_part_size * sizeof(double), __builtin_object_size (src0, 0));
            fir_quantum_double(ctx, s->fadein[0], ch, offset, 0, selir);
            for (int n = 0; n < min_part_size; n++)
                dst[n] = xfade1[n] * src0[n] + xfade0[n] * in[n];
        } else if (!ctx->is_disabled && s->prev_is_disabled) {
            __builtin___memset_chk (src1, 0, min_part_size * sizeof(double), __builtin_object_size (src1, 0));
            fir_quantum_double(ctx, s->fadein[1], ch, offset, 0, selir);
            for (int n = 0; n < min_part_size; n++)
                dst[n] = xfade1[n] * in[n] + xfade0[n] * src1[n];
        } else {
            __builtin___memcpy_chk (dst, in, sizeof(double) * min_part_size, __builtin_object_size (dst, 0));
        }
    } else if (prev_selir != selir && s->loading[ch] != 0) {
        const double *xfade0 = (const double *)s->xfade[0]->extended_data[ch];
        const double *xfade1 = (const double *)s->xfade[1]->extended_data[ch];
        double *src0 = (double *)s->fadein[0]->extended_data[ch];
        double *src1 = (double *)s->fadein[1]->extended_data[ch];
        double *dst = ((double *)out->extended_data[ch]) + offset;

        __builtin___memset_chk (src0, 0, min_part_size * sizeof(double), __builtin_object_size (src0, 0));
        __builtin___memset_chk (src1, 0, min_part_size * sizeof(double), __builtin_object_size (src1, 0));

        fir_quantum_double(ctx, s->fadein[0], ch, offset, 0, prev_selir);
        fir_quantum_double(ctx, s->fadein[1], ch, offset, 0, selir);

        if (s->loading[ch] > s->max_offset[selir]) {
            for (int n = 0; n < min_part_size; n++)
                dst[n] = xfade1[n] * src0[n] + xfade0[n] * src1[n];
            s->loading[ch] = 0;
        } else {
            __builtin___memcpy_chk (dst, src0, min_part_size * sizeof(double), __builtin_object_size (dst, 0));
        }
    } else {
        fir_quantum_double(ctx, out, ch, offset, offset, selir);
    }
}
# 55 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c" 2

static int fir_channel(AVFilterContext *ctx, AVFrame *out, int ch)
{
    AudioFIRContext *s = ctx->priv;
    const int min_part_size = s->min_part_size;
    const int prev_selir = s->prev_selir;
    const int selir = s->selir;

    for (int offset = 0; offset < out->nb_samples; offset += min_part_size) {
        switch (s->format) {
        case AV_SAMPLE_FMT_FLTP:
            fir_quantums_float(ctx, s, out, min_part_size, ch, offset, prev_selir, selir);
            break;
        case AV_SAMPLE_FMT_DBLP:
            fir_quantums_double(ctx, s, out, min_part_size, ch, offset, prev_selir, selir);
            break;
        }

        if (selir != prev_selir && s->loading[ch] != 0)
            s->loading[ch] += min_part_size;
    }

    return 0;
}

static int fir_channels(AVFilterContext *ctx, void *arg, int jobnr, int nb_jobs)
{
    AVFrame *out = arg;
    const int start = (out->ch_layout.nb_channels * jobnr) / nb_jobs;
    const int end = (out->ch_layout.nb_channels * (jobnr+1)) / nb_jobs;

    for (int ch = start; ch < end; ch++)
        fir_channel(ctx, out, ch);

    return 0;
}

static int fir_frame(AudioFIRContext *s, AVFrame *in, AVFilterLink *outlink)
{
    AVFilterContext *ctx = outlink->src;
    AVFrame *out;

    out = ff_get_audio_buffer(outlink, in->nb_samples);
    if (!out) {
        av_frame_free(&in);
        return (-(12));
    }
    av_frame_copy_props(out, in);
    out->pts = s->pts = in->pts;

    s->in = in;
    ff_filter_execute(ctx, fir_channels, out, ((void*)0),
                      ((outlink->ch_layout.nb_channels) > (ff_filter_get_nb_threads(ctx)) ? (ff_filter_get_nb_threads(ctx)) : (outlink->ch_layout.nb_channels)));
    s->prev_is_disabled = ctx->is_disabled;

    av_frame_free(&in);
    s->in = ((void*)0);

    return ff_filter_frame(outlink, out);
}

static int init_segment(AVFilterContext *ctx, AudioFIRSegment *seg, int selir,
                        int offset, int nb_partitions, int part_size, int index)
{
    AudioFIRContext *s = ctx->priv;
    const size_t cpu_align = av_cpu_max_align();
    union { double d; float f; } cscale, scale, iscale;
    enum AVTXType tx_type;
    int ret;

    seg->tx = av_calloc(ctx->inputs[0]->ch_layout.nb_channels, sizeof(*seg->tx));
    seg->ctx = av_calloc(ctx->inputs[0]->ch_layout.nb_channels, sizeof(*seg->ctx));
    seg->itx = av_calloc(ctx->inputs[0]->ch_layout.nb_channels, sizeof(*seg->itx));
    if (!seg->tx || !seg->ctx || !seg->itx)
        return (-(12));

    seg->fft_length = (part_size + 1) * 2;
    seg->part_size = part_size;
    seg->coeff_size = (((seg->part_size + 1)+(cpu_align)-1)&~((cpu_align)-1));
    seg->block_size = ((seg->coeff_size * 2) > ((((seg->fft_length)+(cpu_align)-1)&~((cpu_align)-1))) ? (seg->coeff_size * 2) : ((((seg->fft_length)+(cpu_align)-1)&~((cpu_align)-1))));
    seg->nb_partitions = nb_partitions;
    seg->input_size = offset + s->min_part_size;
    seg->input_offset = offset;

    seg->part_index = av_calloc(ctx->inputs[0]->ch_layout.nb_channels, sizeof(*seg->part_index));
    seg->output_offset = av_calloc(ctx->inputs[0]->ch_layout.nb_channels, sizeof(*seg->output_offset));
    if (!seg->part_index || !seg->output_offset)
        return (-(12));

    switch (s->format) {
    case AV_SAMPLE_FMT_FLTP:
        cscale.f = 1.f;
        scale.f = 1.f / sqrtf(2.f * part_size);
        iscale.f = 1.f / sqrtf(2.f * part_size);
        tx_type = AV_TX_FLOAT_RDFT;
        break;
    case AV_SAMPLE_FMT_DBLP:
        cscale.d = 1.0;
        scale.d = 1.0 / sqrt(2.0 * part_size);
        iscale.d = 1.0 / sqrt(2.0 * part_size);
        tx_type = AV_TX_DOUBLE_RDFT;
        break;
    }

    for (int ch = 0; ch < ctx->inputs[0]->ch_layout.nb_channels && part_size >= 1; ch++) {
        ret = av_tx_init(&seg->ctx[ch], &seg->ctx_fn, tx_type,
                         0, 2 * part_size, &cscale, 0);
        if (ret < 0)
            return ret;

        ret = av_tx_init(&seg->tx[ch], &seg->tx_fn, tx_type,
                         0, 2 * part_size, &scale, 0);
        if (ret < 0)
            return ret;
        ret = av_tx_init(&seg->itx[ch], &seg->itx_fn, tx_type,
                         1, 2 * part_size, &iscale, 0);
        if (ret < 0)
            return ret;
    }

    seg->sumin = ff_get_audio_buffer(ctx->inputs[0], seg->fft_length);
    seg->sumout = ff_get_audio_buffer(ctx->inputs[0], seg->fft_length);
    seg->blockout = ff_get_audio_buffer(ctx->inputs[0], seg->block_size * seg->nb_partitions);
    seg->tempin = ff_get_audio_buffer(ctx->inputs[0], seg->block_size);
    seg->tempout = ff_get_audio_buffer(ctx->inputs[0], seg->block_size);
    seg->buffer = ff_get_audio_buffer(ctx->inputs[0], seg->part_size);
    seg->input = ff_get_audio_buffer(ctx->inputs[0], seg->input_size);
    seg->output = ff_get_audio_buffer(ctx->inputs[0], seg->part_size * 5);
    if (!seg->buffer || !seg->sumin || !seg->sumout || !seg->blockout ||
        !seg->input || !seg->output || !seg->tempin || !seg->tempout)
        return (-(12));

    return 0;
}

static void uninit_segment(AVFilterContext *ctx, AudioFIRSegment *seg)
{
    AudioFIRContext *s = ctx->priv;

    if (seg->ctx) {
        for (int ch = 0; ch < s->nb_channels; ch++)
            av_tx_uninit(&seg->ctx[ch]);
    }
    av_freep(&seg->ctx);

    if (seg->tx) {
        for (int ch = 0; ch < s->nb_channels; ch++)
            av_tx_uninit(&seg->tx[ch]);
    }
    av_freep(&seg->tx);

    if (seg->itx) {
        for (int ch = 0; ch < s->nb_channels; ch++)
            av_tx_uninit(&seg->itx[ch]);
    }
    av_freep(&seg->itx);

    av_freep(&seg->output_offset);
    av_freep(&seg->part_index);

    av_frame_free(&seg->tempin);
    av_frame_free(&seg->tempout);
    av_frame_free(&seg->blockout);
    av_frame_free(&seg->sumin);
    av_frame_free(&seg->sumout);
    av_frame_free(&seg->buffer);
    av_frame_free(&seg->input);
    av_frame_free(&seg->output);
    seg->input_size = 0;

    for (int i = 0; i < 32; i++)
        av_frame_free(&seg->coeff);
}

static int convert_coeffs(AVFilterContext *ctx, int selir)
{
    AudioFIRContext *s = ctx->priv;
    int ret, nb_taps, cur_nb_taps;

    if (!s->nb_taps[selir]) {
        int part_size, max_part_size;
        int left, offset = 0;

        s->nb_taps[selir] = ff_inlink_queued_samples(ctx->inputs[1 + selir]);
        if (s->nb_taps[selir] <= 0)
            return (-(22));

        if (s->minp > s->maxp)
            s->maxp = s->minp;

        if (s->nb_segments[selir])
            goto skip;

        left = s->nb_taps[selir];
        part_size = 1 << av_log2(s->minp);
        max_part_size = 1 << av_log2(s->maxp);

        for (int i = 0; left > 0; i++) {
            int step = (part_size == max_part_size) ? 2147483647 : 1 + (i == 0);
            int nb_partitions = ((step) > ((left + part_size - 1) / part_size) ? ((left + part_size - 1) / part_size) : (step));

            s->nb_segments[selir] = i + 1;
            ret = init_segment(ctx, &s->seg[selir][i], selir, offset, nb_partitions, part_size, i);
            if (ret < 0)
                return ret;
            offset += nb_partitions * part_size;
            s->max_offset[selir] = offset;
            left -= nb_partitions * part_size;
            part_size *= 2;
            part_size = ((part_size) > (max_part_size) ? (max_part_size) : (part_size));
        }
    }

skip:
    if (!s->ir[selir]) {
        ret = ff_inlink_consume_samples(ctx->inputs[1 + selir], s->nb_taps[selir], s->nb_taps[selir], &s->ir[selir]);
        if (ret < 0)
            return ret;
        if (ret == 0)
            return (-(int)(('B') | (('U') << 8) | (('G') << 16) | ((unsigned)('!') << 24)));
    }

    cur_nb_taps = s->ir[selir]->nb_samples;
    nb_taps = cur_nb_taps;

    if (!s->norm_ir[selir] || s->norm_ir[selir]->nb_samples < nb_taps) {
        av_frame_free(&s->norm_ir[selir]);
        s->norm_ir[selir] = ff_get_audio_buffer(ctx->inputs[0], (((nb_taps)+(8)-1)&~((8)-1)));
        if (!s->norm_ir[selir])
            return (-(12));
    }

    av_log(ctx, 48, "nb_taps: %d\n", cur_nb_taps);
    av_log(ctx, 48, "nb_segments: %d\n", s->nb_segments[selir]);

    switch (s->format) {
    case AV_SAMPLE_FMT_FLTP:
        for (int ch = 0; ch < s->nb_channels; ch++) {
            const float *tsrc = (const float *)s->ir[selir]->extended_data[!s->one2many * ch];

            s->ch_gain[ch] = ir_gain_float(ctx, s, nb_taps, tsrc);
        }

        if (s->ir_link) {
            float gain = +__builtin_huge_valf();

            for (int ch = 0; ch < s->nb_channels; ch++)
                gain = fminf(gain, s->ch_gain[ch]);

            for (int ch = 0; ch < s->nb_channels; ch++)
                s->ch_gain[ch] = gain;
        }

        for (int ch = 0; ch < s->nb_channels; ch++) {
            const float *tsrc = (const float *)s->ir[selir]->extended_data[!s->one2many * ch];
            float *time = (float *)s->norm_ir[selir]->extended_data[ch];

            __builtin___memcpy_chk (time, tsrc, sizeof(*time) * nb_taps, __builtin_object_size (time, 0));
            for (int i = ((1) > (s->length * nb_taps) ? (1) : (s->length * nb_taps)); i < nb_taps; i++)
                time[i] = 0;

            ir_scale_float(ctx, s, nb_taps, ch, time, s->ch_gain[ch]);

            for (int n = 0; n < s->nb_segments[selir]; n++) {
                AudioFIRSegment *seg = &s->seg[selir][n];

                if (!seg->coeff)
                    seg->coeff = ff_get_audio_buffer(ctx->inputs[0], seg->nb_partitions * seg->coeff_size * 2);
                if (!seg->coeff)
                    return (-(12));

                for (int i = 0; i < seg->nb_partitions; i++)
                    convert_channel_float(ctx, s, ch, seg, i, selir);
            }
        }
        break;
    case AV_SAMPLE_FMT_DBLP:
        for (int ch = 0; ch < s->nb_channels; ch++) {
            const double *tsrc = (const double *)s->ir[selir]->extended_data[!s->one2many * ch];

            s->ch_gain[ch] = ir_gain_double(ctx, s, nb_taps, tsrc);
        }

        if (s->ir_link) {
            double gain = +__builtin_huge_valf();

            for (int ch = 0; ch < s->nb_channels; ch++)
                gain = fmin(gain, s->ch_gain[ch]);

            for (int ch = 0; ch < s->nb_channels; ch++)
                s->ch_gain[ch] = gain;
        }

        for (int ch = 0; ch < s->nb_channels; ch++) {
            const double *tsrc = (const double *)s->ir[selir]->extended_data[!s->one2many * ch];
            double *time = (double *)s->norm_ir[selir]->extended_data[ch];

            __builtin___memcpy_chk (time, tsrc, sizeof(*time) * nb_taps, __builtin_object_size (time, 0));
            for (int i = ((1) > (s->length * nb_taps) ? (1) : (s->length * nb_taps)); i < nb_taps; i++)
                time[i] = 0;

            ir_scale_double(ctx, s, nb_taps, ch, time, s->ch_gain[ch]);

            for (int n = 0; n < s->nb_segments[selir]; n++) {
                AudioFIRSegment *seg = &s->seg[selir][n];

                if (!seg->coeff)
                    seg->coeff = ff_get_audio_buffer(ctx->inputs[0], seg->nb_partitions * seg->coeff_size * 2);
                if (!seg->coeff)
                    return (-(12));

                for (int i = 0; i < seg->nb_partitions; i++)
                    convert_channel_double(ctx, s, ch, seg, i, selir);
            }
        }
        break;
    }

    s->have_coeffs[selir] = 1;

    return 0;
}

static int check_ir(AVFilterLink *link, int selir)
{
    AVFilterContext *ctx = link->dst;
    AudioFIRContext *s = ctx->priv;
    int nb_taps, max_nb_taps;

    nb_taps = ff_inlink_queued_samples(link);
    max_nb_taps = s->max_ir_len * ctx->outputs[0]->sample_rate;
    if (nb_taps > max_nb_taps) {
        av_log(ctx, 16, "Too big number of coefficients: %d > %d.\n", nb_taps, max_nb_taps);
        return (-(22));
    }

    if (ff_inlink_check_available_samples(link, nb_taps + 1) == 1)
        s->eof_coeffs[selir] = 1;

    return 0;
}

static int activate(AVFilterContext *ctx)
{
    AudioFIRContext *s = ctx->priv;
    AVFilterLink *outlink = ctx->outputs[0];
    int ret, status, available, wanted;
    AVFrame *in = ((void*)0);
    int64_t pts;

    do { int ret = ff_outlink_get_status(ctx->outputs[0]); if (ret) { unsigned i; for (i = 0; i < ctx->nb_inputs; i++) ff_inlink_set_status(ctx->inputs[i], ret); return 0; } } while (0);

    for (int i = 0; i < s->nb_irs; i++) {
        const int selir = i;

        if (s->ir_load && selir != s->selir)
            continue;

        if (!s->eof_coeffs[selir]) {
            ret = check_ir(ctx->inputs[1 + selir], selir);
            if (ret < 0)
                return ret;

            if (!s->eof_coeffs[selir]) {
                if (ff_outlink_frame_wanted(ctx->outputs[0]))
                    ff_inlink_request_frame(ctx->inputs[1 + selir]);
                return 0;
            }
        }

        if (!s->have_coeffs[selir] && s->eof_coeffs[selir]) {
            ret = convert_coeffs(ctx, selir);
            if (ret < 0)
                return ret;
        }
    }

    available = ff_inlink_queued_samples(ctx->inputs[0]);
    wanted = ((s->min_part_size) > ((available / s->min_part_size) * s->min_part_size) ? (s->min_part_size) : ((available / s->min_part_size) * s->min_part_size));
    ret = ff_inlink_consume_samples(ctx->inputs[0], wanted, wanted, &in);
    if (ret > 0)
        ret = fir_frame(s, in, outlink);

    if (s->selir != s->prev_selir && s->loading[0] == 0)
        s->prev_selir = s->selir;

    if (ret < 0)
        return ret;

    if (ff_inlink_queued_samples(ctx->inputs[0]) >= s->min_part_size) {
        ff_filter_set_ready(ctx, 10);
        return 0;
    }

    if (ff_inlink_acknowledge_status(ctx->inputs[0], &status, &pts)) {
        if (status == (-(int)(('E') | (('O') << 8) | (('F') << 16) | ((unsigned)(' ') << 24)))) {
            ff_outlink_set_status(ctx->outputs[0], status, pts);
            return 0;
        }
    }

    if (ff_outlink_frame_wanted(ctx->outputs[0])) {
        ff_inlink_request_frame(ctx->inputs[0]);
        return 0;
    }

    return (-(int)(('N') | (('R') << 8) | (('D') << 16) | ((unsigned)('Y') << 24)));
}

static int query_formats(AVFilterContext *ctx)
{
    AudioFIRContext *s = ctx->priv;
    static const enum AVSampleFormat sample_fmts[3][3] = {
        { AV_SAMPLE_FMT_FLTP, AV_SAMPLE_FMT_DBLP, AV_SAMPLE_FMT_NONE },
        { AV_SAMPLE_FMT_FLTP, AV_SAMPLE_FMT_NONE },
        { AV_SAMPLE_FMT_DBLP, AV_SAMPLE_FMT_NONE },
    };
    int ret;

    if (s->ir_format) {
        ret = ff_set_common_all_channel_counts(ctx);
        if (ret < 0)
            return ret;
    } else {
        AVFilterChannelLayouts *mono = ((void*)0);
        AVFilterChannelLayouts *layouts = ff_all_channel_counts();

        if ((ret = ff_channel_layouts_ref(layouts, &ctx->inputs[0]->outcfg.channel_layouts)) < 0)
            return ret;
        if ((ret = ff_channel_layouts_ref(layouts, &ctx->outputs[0]->incfg.channel_layouts)) < 0)
            return ret;

        ret = ff_add_channel_layout(&mono, &(AVChannelLayout){ AV_CHANNEL_ORDER_NATIVE, (1), { ((1ULL << AV_CHAN_FRONT_CENTER )) }, ((void*)0) });
        if (ret)
            return ret;
        for (int i = 1; i < ctx->nb_inputs; i++) {
            if ((ret = ff_channel_layouts_ref(mono, &ctx->inputs[i]->outcfg.channel_layouts)) < 0)
                return ret;
        }
    }

    if ((ret = ff_set_common_formats_from_list(ctx, sample_fmts[s->precision])) < 0)
        return ret;

    return ff_set_common_all_samplerates(ctx);
}

static int config_output(AVFilterLink *outlink)
{
    AVFilterContext *ctx = outlink->src;
    AudioFIRContext *s = ctx->priv;
    int ret;

    s->one2many = ctx->inputs[1 + s->selir]->ch_layout.nb_channels == 1;
    outlink->sample_rate = ctx->inputs[0]->sample_rate;
    outlink->time_base = ctx->inputs[0]->time_base;

#pragma GCC diagnostic push
# 512 "/Users/davidchen/repo/ffmpeg/libavfilter/af_afir.c"
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
    outlink->channel_layout = ctx->inputs[0]->channel_layout;
#pragma GCC diagnostic pop

    if ((ret = av_channel_layout_copy(&outlink->ch_layout, &ctx->inputs[0]->ch_layout)) < 0)
        return ret;
    outlink->ch_layout.nb_channels = ctx->inputs[0]->ch_layout.nb_channels;

    s->format = outlink->format;
    s->nb_channels = outlink->ch_layout.nb_channels;
    s->ch_gain = av_calloc(ctx->inputs[0]->ch_layout.nb_channels, sizeof(*s->ch_gain));
    s->loading = av_calloc(ctx->inputs[0]->ch_layout.nb_channels, sizeof(*s->loading));
    if (!s->loading || !s->ch_gain)
        return (-(12));

    s->fadein[0] = ff_get_audio_buffer(outlink, s->min_part_size);
    s->fadein[1] = ff_get_audio_buffer(outlink, s->min_part_size);
    if (!s->fadein[0] || !s->fadein[1])
        return (-(12));

    s->xfade[0] = ff_get_audio_buffer(outlink, s->min_part_size);
    s->xfade[1] = ff_get_audio_buffer(outlink, s->min_part_size);
    if (!s->xfade[0] || !s->xfade[1])
        return (-(12));

    switch (s->format) {
    case AV_SAMPLE_FMT_FLTP:
        for (int ch = 0; ch < s->nb_channels; ch++) {
            float *dst0 = (float *)s->xfade[0]->extended_data[ch];
            float *dst1 = (float *)s->xfade[1]->extended_data[ch];

            for (int n = 0; n < s->min_part_size; n++) {
                dst0[n] = (n + 1.f) / s->min_part_size;
                dst1[n] = 1.f - dst0[n];
            }
        }
        break;
    case AV_SAMPLE_FMT_DBLP:
        for (int ch = 0; ch < s->nb_channels; ch++) {
            double *dst0 = (double *)s->xfade[0]->extended_data[ch];
            double *dst1 = (double *)s->xfade[1]->extended_data[ch];

            for (int n = 0; n < s->min_part_size; n++) {
                dst0[n] = (n + 1.0) / s->min_part_size;
                dst1[n] = 1.0 - dst0[n];
            }
        }
        break;
    }

    return 0;
}

static __attribute__((cold)) void uninit(AVFilterContext *ctx)
{
    AudioFIRContext *s = ctx->priv;

    av_freep(&s->fdsp);
    av_freep(&s->ch_gain);
    av_freep(&s->loading);

    for (int i = 0; i < s->nb_irs; i++) {
        for (int j = 0; j < s->nb_segments[i]; j++)
            uninit_segment(ctx, &s->seg[i][j]);

        av_frame_free(&s->ir[i]);
        av_frame_free(&s->norm_ir[i]);
    }

    av_frame_free(&s->fadein[0]);
    av_frame_free(&s->fadein[1]);

    av_frame_free(&s->xfade[0]);
    av_frame_free(&s->xfade[1]);
}

static __attribute__((cold)) int init(AVFilterContext *ctx)
{
    AudioFIRContext *s = ctx->priv;
    AVFilterPad pad;
    int ret;

    s->prev_selir = ((s->nb_irs - 1) > (s->selir) ? (s->selir) : (s->nb_irs - 1));

    pad = (AVFilterPad) {
        .name = "main",
        .type = AVMEDIA_TYPE_AUDIO,
    };

    ret = ff_append_inpad(ctx, &pad);
    if (ret < 0)
        return ret;

    for (int n = 0; n < s->nb_irs; n++) {
        pad = (AVFilterPad) {
            .name = av_asprintf("ir%d", n),
            .type = AVMEDIA_TYPE_AUDIO,
        };

        if (!pad.name)
            return (-(12));

        ret = ff_append_inpad_free_name(ctx, &pad);
        if (ret < 0)
            return ret;
    }

    s->fdsp = avpriv_float_dsp_alloc(0);
    if (!s->fdsp)
        return (-(12));

    ff_afir_init(&s->afirdsp);

    s->min_part_size = 1 << av_log2(s->minp);
    s->max_part_size = 1 << av_log2(s->maxp);

    return 0;
}

static int process_command(AVFilterContext *ctx,
                           const char *cmd,
                           const char *arg,
                           char *res,
                           int res_len,
                           int flags)
{
    AudioFIRContext *s = ctx->priv;
    int prev_selir, ret;

    prev_selir = s->selir;
    ret = ff_filter_process_command(ctx, cmd, arg, res, res_len, flags);
    if (ret < 0)
        return ret;

    s->selir = ((s->nb_irs - 1) > (s->selir) ? (s->selir) : (s->nb_irs - 1));
    if (s->selir != prev_selir) {
        s->prev_selir = prev_selir;

        for (int ch = 0; ch < s->nb_channels; ch++)
            s->loading[ch] = 1;
    }

    return 0;
}






static const AVOption afir_options[] = {
    { "dry", "set dry gain", __builtin_offsetof(AudioFIRContext, dry_gain), AV_OPT_TYPE_FLOAT, {.dbl=1}, 0, 10, 8|(1<<16)|(1<<15) },
    { "wet", "set wet gain", __builtin_offsetof(AudioFIRContext, wet_gain), AV_OPT_TYPE_FLOAT, {.dbl=1}, 0, 10, 8|(1<<16)|(1<<15) },
    { "length", "set IR length", __builtin_offsetof(AudioFIRContext, length), AV_OPT_TYPE_FLOAT, {.dbl=1}, 0, 1, 8|(1<<16) },
    { "gtype", "set IR auto gain type",__builtin_offsetof(AudioFIRContext, gtype), AV_OPT_TYPE_INT, {.i64=0}, -1, 4, 8|(1<<16)|(1<<17), "gtype" },
    { "none", "without auto gain", 0, AV_OPT_TYPE_CONST, {.i64=-1}, 0, 0, 8|(1<<16)|(1<<17), "gtype" },
    { "peak", "peak gain", 0, AV_OPT_TYPE_CONST, {.i64=0}, 0, 0, 8|(1<<16)|(1<<17), "gtype" },
    { "dc", "DC gain", 0, AV_OPT_TYPE_CONST, {.i64=1}, 0, 0, 8|(1<<16)|(1<<17), "gtype" },
    { "gn", "gain to noise", 0, AV_OPT_TYPE_CONST, {.i64=2}, 0, 0, 8|(1<<16)|(1<<17), "gtype" },
    { "ac", "AC gain", 0, AV_OPT_TYPE_CONST, {.i64=3}, 0, 0, 8|(1<<16)|(1<<17), "gtype" },
    { "rms", "RMS gain", 0, AV_OPT_TYPE_CONST, {.i64=4}, 0, 0, 8|(1<<16)|(1<<17), "gtype" },
    { "irnorm", "set IR norm", __builtin_offsetof(AudioFIRContext, ir_norm), AV_OPT_TYPE_FLOAT, {.dbl=1}, -1, 2, 8|(1<<16) },
    { "irlink", "set IR link", __builtin_offsetof(AudioFIRContext, ir_link), AV_OPT_TYPE_BOOL, {.i64=1}, 0, 1, 8|(1<<16) },
    { "irgain", "set IR gain", __builtin_offsetof(AudioFIRContext, ir_gain), AV_OPT_TYPE_FLOAT, {.dbl=1}, 0, 1, 8|(1<<16) },
    { "irfmt", "set IR format", __builtin_offsetof(AudioFIRContext, ir_format), AV_OPT_TYPE_INT, {.i64=1}, 0, 1, 8|(1<<16), "irfmt" },
    { "mono", "single channel", 0, AV_OPT_TYPE_CONST, {.i64=0}, 0, 0, 8|(1<<16), "irfmt" },
    { "input", "same as input", 0, AV_OPT_TYPE_CONST, {.i64=1}, 0, 0, 8|(1<<16), "irfmt" },
    { "maxir", "set max IR length", __builtin_offsetof(AudioFIRContext, max_ir_len), AV_OPT_TYPE_FLOAT, {.dbl=30}, 0.1, 60, 8|(1<<16) },
    { "response", "show IR frequency response", __builtin_offsetof(AudioFIRContext, response), AV_OPT_TYPE_BOOL, {.i64=0}, 0, 1, 16|(1<<16)|(1<<17) },
    { "channel", "set IR channel to display frequency response", __builtin_offsetof(AudioFIRContext, ir_channel), AV_OPT_TYPE_INT, {.i64=0}, 0, 1024, 16|(1<<16)|(1<<17) },
    { "size", "set video size", __builtin_offsetof(AudioFIRContext, w), AV_OPT_TYPE_IMAGE_SIZE, {.str = "hd720"}, 0, 0, 16|(1<<16)|(1<<17) },
    { "rate", "set video rate", __builtin_offsetof(AudioFIRContext, frame_rate), AV_OPT_TYPE_VIDEO_RATE, {.str = "25"}, 0, 2147483647, 16|(1<<16)|(1<<17) },
    { "minp", "set min partition size", __builtin_offsetof(AudioFIRContext, minp), AV_OPT_TYPE_INT, {.i64=8192}, 1, 65536, 8|(1<<16) },
    { "maxp", "set max partition size", __builtin_offsetof(AudioFIRContext, maxp), AV_OPT_TYPE_INT, {.i64=8192}, 8, 65536, 8|(1<<16) },
    { "nbirs", "set number of input IRs",__builtin_offsetof(AudioFIRContext, nb_irs),AV_OPT_TYPE_INT, {.i64=1}, 1, 32, 8|(1<<16) },
    { "ir", "select IR", __builtin_offsetof(AudioFIRContext, selir), AV_OPT_TYPE_INT, {.i64=0}, 0, 31, 8|(1<<16)|(1<<15) },
    { "precision", "set processing precision", __builtin_offsetof(AudioFIRContext, precision), AV_OPT_TYPE_INT, {.i64=0}, 0, 2, 8|(1<<16), "precision" },
    { "auto", "set auto processing precision", 0, AV_OPT_TYPE_CONST, {.i64=0}, 0, 0, 8|(1<<16), "precision" },
    { "float", "set single-floating point processing precision", 0, AV_OPT_TYPE_CONST, {.i64=1}, 0, 0, 8|(1<<16), "precision" },
    { "double","set double-floating point processing precision", 0, AV_OPT_TYPE_CONST, {.i64=2}, 0, 0, 8|(1<<16), "precision" },
    { "irload", "set IR loading type", __builtin_offsetof(AudioFIRContext, ir_load), AV_OPT_TYPE_INT, {.i64=0}, 0, 1, 8|(1<<16), "irload" },
    { "init", "load all IRs on init", 0, AV_OPT_TYPE_CONST, {.i64=0}, 0, 0, 8|(1<<16), "irload" },
    { "access", "load IR on access", 0, AV_OPT_TYPE_CONST, {.i64=1}, 0, 0, 8|(1<<16), "irload" },
    { ((void*)0) }
};

static const AVClass afir_class = { .class_name = "afir", .item_name = av_default_item_name, .option = afir_options, .version = ((58)<<16 | (36)<<8 | (100)), .category = AV_CLASS_CATEGORY_FILTER, };

static const AVFilterPad outputs[] = {
    {
        .name = "default",
        .type = AVMEDIA_TYPE_AUDIO,
        .config_props = config_output,
    },
};

const AVFilter ff_af_afir = {
    .name = "afir",
    .description = "Apply Finite Impulse Response filter with supplied coefficients in additional stream(s).",
    .priv_size = sizeof(AudioFIRContext),
    .priv_class = &afir_class,
    .formats.query_func = query_formats, .formats_state = FF_FILTER_FORMATS_QUERY_FUNC,
    .outputs = (outputs), .nb_outputs = (sizeof((outputs)) / sizeof(((outputs))[0])),
    .init = init,
    .activate = activate,
    .uninit = uninit,
    .process_command = process_command,
    .flags = (1 << 0) |
                     (1 << 17) |
                     (1 << 2),
};